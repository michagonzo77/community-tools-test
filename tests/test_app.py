import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_nonexistent_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404