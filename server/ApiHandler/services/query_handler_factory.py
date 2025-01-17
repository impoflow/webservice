from services.lambda_query_handler import LambdaQueryHandler

lambda_function_name = "neo4j_query_handler_function"

class QueryHandlerFactory:
    """
    Fábrica para crear el tipo de QueryHandler solicitado ('lambda', 'file', etc.).
    """

    def create_query_handler(self, handler_type: str):
        if handler_type == "lambda":
            return LambdaQueryHandler(function_name=lambda_function_name)
        else:
            return None
