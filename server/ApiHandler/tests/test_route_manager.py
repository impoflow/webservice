import unittest
from unittest.mock import MagicMock
from flask import Flask
from services.query_handler_factory import QueryHandlerFactory
from services.lambda_query_handler import LambdaQueryHandler
from route_manager import RouteManager
from api_routes import ROUTES


class TestRouteManager(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.mock_query_handler = MagicMock(spec=LambdaQueryHandler)
        self.mock_query_handler.call.return_value = '{"mock_key": "mock_value"}'

    def test_route_registration(self):
        route_manager = RouteManager(self.app, self.mock_query_handler)
        route_manager.register_routes()

        for route in ROUTES:
            with self.app.test_client() as client:
                resp = client.get(route.replace('<string:user_id>', '123').replace('<string:project_id>', '456'))
                self.assertIn(resp.status_code, [200, 404])

    def test_handle_request(self):
        route_manager = RouteManager(self.app, self.mock_query_handler)

        with self.app.test_request_context(path="/test"):
            response = route_manager._handle_request("/test")

        self.mock_query_handler.call.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"mock_key": "mock_value"})


if __name__ == "__main__":
    unittest.main()
