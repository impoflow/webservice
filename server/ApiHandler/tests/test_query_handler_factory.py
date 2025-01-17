import unittest
from services.query_handler_factory import QueryHandlerFactory
from services.lambda_query_handler import LambdaQueryHandler


class TestQueryHandlerFactory(unittest.TestCase):
    def test_query_handler_factory_lambda(self):
        factory = QueryHandlerFactory()
        handler = factory.create_query_handler("lambda")
        self.assertIsInstance(handler, LambdaQueryHandler)

    def test_query_handler_factory_none(self):
        factory = QueryHandlerFactory()
        handler = factory.create_query_handler("file")
        self.assertIsNone(handler)


if __name__ == "__main__":
    unittest.main()
