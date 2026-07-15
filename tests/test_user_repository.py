from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import user_repository
import uuid

def test_create_user(db):

    email = f"{uuid.uuid4()}@test.com"

    user = User(
        name="Repository Test",
        email=email,
        hashed_password=hash_password("password123"),
    )

    saved_user = user_repository.create_user(
        db,
        user,
    )

    assert saved_user.id is not None
    assert saved_user.email == email

