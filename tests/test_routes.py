import pytest
from app import app

@pytest.fixture
def client():
    """Fixture to set up a Flask test client."""
    with app.test_client() as client:
        yield client

def test_home_route_invalid_method(client):
    """
    Test that the home route returns 405 when an invalid method is used.
    Purpose: Ensures the route has proper HTTP method handling.
    """
    response = client.post('/')  # Using POST instead of GET
    assert response.status_code == 405  # Method Not Allowed
