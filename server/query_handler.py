import boto3
from abc import ABC, abstractmethod


lambda_function_name = "neo4j_query_handler_function"


class QueryHandler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def call(self, function_name, payload):
        pass


class LambdaQueryHandler(QueryHandler):
    def __init__(self, function_name):
        self.client = boto3.client('lambda', region_name='us-east-1')
        self.function_name = function_name

    def call(self, payload):
        response = self.client.invoke(
            FunctionName=self.function_name,
            InvocationType='RequestResponse',
            Payload=payload
        )
        return response['Payload'].read()
    

class QueryHandlerFactory:
    def __init__(self):
        pass

    def create_query_handler(self, type):
        if type == "lambda":
            return LambdaQueryHandler(lambda_function_name)
        else:
            return None
