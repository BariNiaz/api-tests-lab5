import requests
from jsonschema import validate
def test_invalid_login():
    response = requests.post("https://reqres.in/api/login", json={"email": "test@test"})
    assert response.status_code == 400
    assert "error" in response.json()
