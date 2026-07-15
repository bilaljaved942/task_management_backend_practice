import uuid

def test_register(client):

    email = f"{uuid.uuid4()}@test.com"

    response = client.post(
        "/auth/register",
        json={
            "name": "Bilal",
            "email": email,
            "password": "password123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == email

    assert "id" in data



def test_register_duplicate_email(client):

    email = f"{uuid.uuid4()}@test.com"

    payload = {
        "name": "Bilal",
        "email": email,
        "password": "password123",
    }

    client.post(
        "/auth/register",
        json=payload,
    )

    response = client.post(
        "/auth/register",
        json=payload,
    )

    assert response.status_code == 409



def test_login(client):

    email = f"{uuid.uuid4()}@test.com"

    payload = {
        "name": "Bilal",
        "email": email,
        "password": "password123",
    }

    client.post(
        "/auth/register",
        json=payload,
    )

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "password123",
        },
    )

    assert response.status_code == 200

    token = response.json()

    assert "access_token" in token

    assert token["token_type"] == "bearer"


def test_invalid_login(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "abc@test.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401



def get_token(client):

    email = f"{uuid.uuid4()}@test.com"

    payload = {
        "name": "Bilal",
        "email": email,
        "password": "password123",
    }

    client.post(
        "/auth/register",
        json=payload,
    )

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": "password123",
        },
    )

    return response.json()["access_token"]


def test_me(client):

    token = get_token(client)

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200

    user = response.json()

    assert "email" in user


def test_me_without_token(client):

    response = client.get("/auth/me")

    assert response.status_code == 401