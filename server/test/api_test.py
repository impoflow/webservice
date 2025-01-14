import pytest
import json

from api_handler import create_app
from api_handler import routes


class MockQueryHandler:
    def call(self, payload):
        return json.dumps({"mock_key": "mock_value"})

@pytest.fixture
def client():
    app = create_app(custom_query_handler=MockQueryHandler())
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_routes(client):
    for route in routes:
        response = client.get(route)
        assert response.status_code == 200
        assert response.json == {"mock_key": "mock_value"}
        assert response.is_json

def test_invalid_route(client):
    response = client.get("/invalid_route")
    assert response.status_code == 404

def test_method_not_allowed(client):
    for route in routes:
        response = client.post(route)  
    assert response.status_code == 405

def test_unusual_parameters(client):
    response = client.get("/user/!@#$%^&*()")
    assert response.status_code in [200, 400, 404]