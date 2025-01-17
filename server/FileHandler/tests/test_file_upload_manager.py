import unittest
from unittest.mock import MagicMock, patch
from services.file_upload_manager import FileUploadManager
from services.validation_service import ValidationService
from services.s3_uploader import S3Uploader
import os

class TestFileUploadManager(unittest.TestCase):
    def setUp(self):
        self.file_path = "test.zip"
        self.user_name = "test_user"
        self.project_name = "test_project"
        self.collaborators = ["collab1", "collab2"]

        self.mock_validation_service = MagicMock(spec=ValidationService)
        self.mock_s3_uploader = MagicMock(spec=S3Uploader)

        self.manager = FileUploadManager(
            file_path=self.file_path,
            user_name=self.user_name,
            project_name=self.project_name,
            collaborators=self.collaborators,
            validation_service=self.mock_validation_service,
            s3_uploader=self.mock_s3_uploader,
        )

    def test_validate_and_upload_success(self):
        self.mock_validation_service.validate_zip_file.return_value = (True, "Validation successful")

        self.mock_s3_uploader.upload_file.return_value = True
        self.mock_s3_uploader.upload_json.return_value = True

        success, message = self.manager.validate_and_upload()

        self.assertTrue(success)
        self.assertEqual(message, "File and metadata validated and uploaded successfully")
        self.mock_validation_service.validate_zip_file.assert_called_once_with(self.file_path)
        self.mock_s3_uploader.upload_file.assert_called()
        self.mock_s3_uploader.upload_json.assert_called()

    def test_validate_and_upload_validation_fails(self):
        self.mock_validation_service.validate_zip_file.return_value = (False, "Validation failed")

        success, message = self.manager.validate_and_upload()

        self.assertFalse(success)
        self.assertEqual(message, "Validation failed")
        self.mock_validation_service.validate_zip_file.assert_called_once_with(self.file_path)
        self.mock_s3_uploader.upload_file.assert_not_called()
        self.mock_s3_uploader.upload_json.assert_not_called()

    def test_validate_and_upload_upload_fails(self):
        self.mock_validation_service.validate_zip_file.return_value = (True, "Validation successful")
        self.mock_s3_uploader.upload_file.return_value = False

        success, message = self.manager.validate_and_upload()

        self.assertFalse(success)
        self.assertEqual(message, "Error uploading ZIP to S3")
        self.mock_s3_uploader.upload_file.assert_called_once()

if __name__ == "__main__":
    unittest.main()
    if os.path.exists("test.zip"):
        os.remove("test.zip")
