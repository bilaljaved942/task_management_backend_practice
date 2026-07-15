import uuid

from app.schemas.user import UserCreate
from app.services.auth_service import auth_service
import pytest
from app.core.exceptions import UserAlreadyExistsError

def test_register_user(db):

    email = f"{uuid.uuid4()}@test.com"

    user = UserCreate(
        name="Bilal",
        email=email,
        password="password123",
    )

    saved_user = auth_service.register_user(
        db,
        user,
    )

    assert saved_user.id is not None
    assert saved_user.email == email


def test_duplicate_email(db):

    email = f"{uuid.uuid4()}@test.com"

    user = UserCreate(
        name="Bilal",
        email=email,
        password="password123",
    )

    auth_service.register_user(
        db,
        user,
    )

    with pytest.raises(
        UserAlreadyExistsError,
    ):

        auth_service.register_user(
            db,
            user,
        )