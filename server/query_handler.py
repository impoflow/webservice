import boto3


class QueryHandler:
    def __init__(self):
        pass

    def call(*args, **kwargs):
        pass

class LambdaQueryHandler(QueryHandler):
    def __init__(self):
        self.lambda_client = boto3.client("lambda")
    
    def call(self, function_name, payload):
        response = self.lambda_client.invoke(
            FunctionName=function_name,
            InvocationType="RequestResponse",
            Payload=payload
        )
        return response

