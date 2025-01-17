import unittest
from unittest.mock import MagicMock
from services.s3_uploader import S3Uploader
import tempfile
import os

class TestS3Uploader(unittest.TestCase):
    def setUp(self):
        self.bucket_name = "test-bucket"
        self.s3_uploader = S3Uploader(bucket_name=self.bucket_name)

        self.mock_s3_client = MagicMock()
        self.s3_uploader.s3_client = self.mock_s3_client

    def test_upload_file_success(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as tmp_file:
            file_path = tmp_file.name
            tmp_file.write(b"Test content")
            tmp_file.flush()
        try:
            self.mock_s3_client.upload_file.return_value = None

            success = self.s3_uploader.upload_file(file_path, "test/test.zip")

            self.assertTrue(success)
            self.mock_s3_client.upload_file.assert_called_once_with(file_path, self.bucket_name, "test/test.zip")
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_upload_file_failure(self):
        self.mock_s3_client.upload_file.side_effect = Exception("Upload failed")
        success = self.s3_uploader.upload_file("test.zip", "test/test.zip")
        self.assertFalse(success)


    def test_upload_json_success(self):
        self.mock_s3_client.put_object.return_value = None  # Simula éxito
        success = self.s3_uploader.upload_json({"key": "value"}, "test/test.json")
        self.assertTrue(success)
        self.mock_s3_client.put_object.assert_called_once()

    def test_upload_json_failure(self):
        self.mock_s3_client.put_object.side_effect = Exception("Upload failed")
        success = self.s3_uploader.upload_json({"key": "value"}, "test/test.json")
        self.assertFalse(success)

if __name__ == "__main__":
    unittest.main()
