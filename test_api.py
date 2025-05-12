import requests
from jsonschema import validate
import pytest

def test_get_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data

schema = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "data": {"type": "array"}
    },
    "required": ["data"]
}

def test_get_users_schema():
    response = requests.get("https://reqres.in/api/users?page=2")
    validate(instance=response.json(), schema=schema)

@pytest.mark.parametrize("name, job", [("Bob", "QA"), ("Eve", "DevOps")])
def test_create_user_params(name, job):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"  # Обязательно указываем API ключ
    }

    response = requests.post(
        "https://reqres.in/api/users",
        json={"name": name, "job": job},
        headers=headers
    )

    assert response.status_code == 201
    response_data = response.json()
    assert "id" in response_data
    assert response_data["id"] is not None
