import pytest

from app.core.security import (
    create_access_token,
    hash_password,
    verify_access_token,
    verify_password,
)


def test_hash_password():

    password = "password123"

    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)


def test_verify_password_success():

    password = "password123"

    hashed = hash_password(password)

    assert verify_password(
        password,
        hashed,
    )


def test_verify_password_failure():

    hashed = hash_password(
        "password123"
    )

    assert not verify_password(
        "wrongpassword",
        hashed,
    )


def test_create_access_token():

    token = create_access_token(
        {
            "sub": "1",
        }
    )

    assert isinstance(token, str)
    assert len(token) > 0


def test_verify_access_token():

    token = create_access_token(
        {
            "sub": "1",
        }
    )

    payload = verify_access_token(
        token
    )

    assert payload["sub"] == "1"


def test_invalid_token():

    with pytest.raises(ValueError):

        verify_access_token(
            "invalid-token"
        )