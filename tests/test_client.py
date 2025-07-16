import pytest
from stancer.client import StancerClient
from unittest.mock import patch, Mock

@pytest.fixture
def client():
    return StancerClient("mdupuis", "111111")

@patch("httpx.Client.post")
def test_authenticate_success(mock_post, client):
    mock_response = Mock(status_code=200)
    mock_response.json.return_value = {"access_token": "fake-token"}
    mock_post.return_value = mock_response

    client.authenticate()

    assert client.token == "fake-token"
    assert client.client.headers["Authorization"] == "Bearer fake-token"

@patch("httpx.Client.get")
@patch.object(StancerClient, "authenticate")
def test_get_identity(mock_auth, mock_get, client):
    client.token = "already-token"

    mock_response = Mock(status_code=200)
    mock_response.json.return_value = {"id": "user_123", "first_name": "Maurice"}
    mock_get.return_value = mock_response

    identity = client.get_identity()
    assert identity["first_name"] == "Maurice"
