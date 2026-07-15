from tests.test_auth_api import get_token

def test_create_task(client):

    token = get_token(client)

    response = client.post(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Learn FastAPI",
            "description": "Testing Tasks",
        },
    )

    assert response.status_code == 201

    task = response.json()

    assert task["title"] == "Learn FastAPI"


def test_get_tasks(client):

    token = get_token(client)

    response = client.get(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200


def test_delete_task(client):

    token = get_token(client)

    created = client.post(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Delete Me",
            "description": "",
        },
    )

    task_id = created.json()["id"]

    response = client.delete(
        f"/tasks/{task_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 204