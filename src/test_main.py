from fastapi.testclient import TestClient
from services.jwt import JWT_SECRET, JWT_ALGORITHM
from main import app
import jwt

client = TestClient(app)

"""
Test that the proxy is doing its job and returning correct headers
"""
def test_upstream_post():
    # shorthands
    response = client.post("/", json={"example": "value"})
    info = response.json()
    headers = info["headers"]
    data = info["data"]
    token = headers["x-my-jwt"]

    # will return error if one of the keys is missing
    claims = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

    # check response code
    assert response.status_code == 200
    assert data == "example=value"

    # Note: could also be done by adding  options={"require": ["iat", "jti", "payload"]}  to jwt.decode
    assert "iat" in claims
    assert "jti" in claims
    assert "payload" in claims

    # check if payload keys are present in the claims dict
    assert "username" in claims["payload"]
    assert "date" in claims["payload"]


"""
Test that the health check is working and returning the right data
"""
def test_status():
    response = client.get("/status")
    info = response.json()

    # check response body for the needed keys
    assert "elapsed_time" in info
    assert "upstream_posts" in info

    assert "minutes" in info["elapsed_time"]
    assert "seconds" in info["elapsed_time"]