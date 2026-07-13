from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse,UserLogin
from app.services.auth_service import auth_service
from app.core.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.token import Token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

#register endpoint
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return auth_service.register_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
#login endpoint
@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """
    Authenticate a user using OAuth2 Password Flow.

    OAuth2PasswordRequestForm always provides:
    - username
    - password

    In this project, username represents the user's email.
    """

    login_data = UserLogin(
        email=form_data.username,
        password=form_data.password,
    )

    try:
        token = auth_service.login_user(
            db,
            login_data,
        )

        return Token(
            access_token=token,
            token_type="bearer",
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )
    
#me endpoint
@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    current_user=Depends(get_current_user),
):
    return current_user