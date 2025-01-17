import json
import boto3
import os
from botocore.exceptions import BotoCoreError, ClientError

class S3Uploader:
    """
    Servicio responsable de la subida de archivos y objetos JSON a un bucket S3.
    """

    def __init__(self, bucket_name: str, aws_region: str = "us-east-1"):
        self.bucket_name = bucket_name
        self.aws_region = aws_region
        self.s3_client = boto3.client("s3", region_name=self.aws_region)

    def upload_file(self, local_path: str, s3_key: str) -> bool:
        """
        Sube un archivo local a un bucket S3 en la ruta especificada (s3_key).
        Retorna True si la subida fue exitosa, False si ocurrió algún error.
        """
        try:
            self.s3_client.upload_file(local_path, self.bucket_name, s3_key)
            os.remove(local_path)  # Elimina el archivo local después de subirlo
            return True
        except (BotoCoreError, ClientError) as e:
            print(f"S3 upload failed for file '{local_path}': {e}")
            return False

    def upload_json(self, data: dict, s3_key: str) -> bool:
        """
        Sube un objeto JSON al bucket S3 en la ruta especificada (s3_key).
        Retorna True si la subida fue exitosa, False si ocurrió algún error.
        """
        try:
            json_string = json.dumps(data, indent=4)
            self.s3_client.put_object(
                Body=json_string,
                Bucket=self.bucket_name,
                Key=s3_key,
                ContentType="application/json"
            )
            return True
        except (BotoCoreError, ClientError) as e:
            print(f"S3 upload failed for JSON data: {e}")
            return False
