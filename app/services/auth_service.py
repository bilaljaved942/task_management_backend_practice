from sqlalchemy.orm import Session

from app.core.exceptions import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
)
from app.core.logging import logger
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate, UserLogin


class AuthService:

    def register_user(
        self,
        db: Session,
        user_data: UserCreate,
    ) -> User:

        existing_user = user_repository.get_user_by_email(
            db,
            user_data.email,
        )

        if existing_user:
            raise UserAlreadyExistsError()

        hashed_password = hash_password(
            user_data.password,
        )

        user = User(
            name=user_data.name,
            email=user_data.email,
            hashed_password=hashed_password,
        )

        saved_user = user_repository.create_user(
            db,
            user,
        )

        logger.info(
            "User %s registered successfully",
            saved_user.email,
        )

        return saved_user

    def login_user(
        self,
        db: Session,
        user_data: UserLogin,
    ) -> str:

        user = user_repository.get_user_by_email(
            db,
            user_data.email,
        )

        if not user:
            logger.warning(
                "Failed login attempt for %s",
                user_data.email,
            )
            raise InvalidCredentialsError()

        if not verify_password(
            user_data.password,
            user.hashed_password,
        ):
            logger.warning(
                "Failed login attempt for %s",
                user_data.email,
            )
            raise InvalidCredentialsError()

        logger.info(
            "User %s logged in",
            user.email,
        )

        return create_access_token(
            {
                "sub": str(user.id),
            }
        )


auth_service = AuthService()