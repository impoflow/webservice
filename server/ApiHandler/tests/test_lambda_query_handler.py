import unittest
import json
from unittest.mock import patch, MagicMock
from botocore.exceptions import BotoCoreError
from services.lambda_query_handler import LambdaQueryHandler


class TestLambdaQueryHandler(unittest.TestCase):
    @patch("boto3.client")
    def test_lambda_query_handler_success(self, mock_boto_client):
        mock_lambda = MagicMock()
        mock_lambda.invoke.return_value = {
            "Payload": MagicMock(read=lambda: b'{"result": "ok"}')
        }
        mock_boto_client.return_value = mock_lambda

        handler = LambdaQueryHandler(function_name="test_function")
        response = handler.call(payload=json.dumps({"test": "data"}))

        self.assertEqual(response, '{"result": "ok"}')
        mock_lambda.invoke.assert_called_once()

    def test_lambda_query_handler_failure(self):
        mock_client = MagicMock()
        mock_client.invoke.side_effect = BotoCoreError()

        handler = LambdaQueryHandler(function_name="test_function", lambda_client=mock_client)
        response = handler.call(payload='{"test": "data"}')

        self.assertIn('"error": "Lambda invocation failed"', response)
        self.assertIn('"details": "BotoCoreError: An unspecified error occurred"', response)


if __name__ == "__main__":
    unittest.main()
