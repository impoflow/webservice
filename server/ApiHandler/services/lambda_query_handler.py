import boto3
from botocore.exceptions import BotoCoreError, ClientError
from services.query_handler import QueryHandler

class LambdaQueryHandler(QueryHandler):
    """
    Implementación del QueryHandler que hace llamadas a una AWS Lambda.
    """

    def __init__(self, function_name: str, aws_region: str = "us-east-1", lambda_client=None):
        self.function_name = function_name
        self.client = lambda_client or boto3.client("lambda", region_name=aws_region)

    def call(self, payload: str) -> str:
        """
        Invoca la Lambda en modo RequestResponse y retorna la respuesta.
        """
        try:
            response = self.client.invoke(
                FunctionName=self.function_name,
                InvocationType="RequestResponse",
                Payload=payload
            )
            return response["Payload"].read().decode("utf-8")
        except (BotoCoreError, ClientError) as e:
            return '{"error": "Lambda invocation failed", "details": "%s: %s"}' % (e.__class__.__name__, str(e))

