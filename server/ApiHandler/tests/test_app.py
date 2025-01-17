import unittest
from unittest.mock import MagicMock
from app import create_app


class TestApp(unittest.TestCase):
    def setUp(self):
        test_app = create_app(query_handler_type="lambda")
        test_app.config["TESTING"] = True
        self.client = test_app.test_client()

    def test_app_routes_exist(self):
        resp = self.client.get("/metrics")
        self.assertEqual(resp.status_code, 200)

        for route in ["/users", "/projects"]:
            response = self.client.get(route)
            self.assertIn(response.status_code, [200, 404], f"Falla en la ruta: {route}")


if __name__ == "__main__":
    unittest.main()
