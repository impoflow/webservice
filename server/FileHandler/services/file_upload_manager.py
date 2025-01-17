import os

class FileUploadManager:
    """
    Orquesta la validación del archivo y su posterior subida a S3.
    También puede almacenar metadata en S3 o localmente.
    """

    def __init__(self, 
                 file_path: str,
                 user_name: str,
                 project_name: str,
                 collaborators: list[str],
                 validation_service,
                 s3_uploader):
        self.file_path = file_path
        self.user_name = user_name
        self.project_name = project_name
        self.collaborators = collaborators
        self.validation_service = validation_service
        self.s3_uploader = s3_uploader

    def validate_and_upload(self) -> tuple[bool, str]:
        """
        - Valida el ZIP.
        - Si es válido, lo sube a S3.
        - Luego sube también la metadata en formato JSON al mismo bucket S3.
        - Retorna (is_success, message).
        """
        is_valid, message = self.validation_service.validate_zip_file(self.file_path)
        if not is_valid:
            return False, message

        zip_s3_key = f"{self.user_name}/{self.project_name}/{os.path.basename(self.file_path)}"
        upload_ok = self.s3_uploader.upload_file(self.file_path, zip_s3_key)
        if not upload_ok:
            return False, "Error uploading ZIP to S3"

        metadata = {
            "user": self.user_name,
            "project_name": self.project_name,
            "collaborators": self.collaborators
        }
        metadata_s3_key = f"{self.user_name}/{self.project_name}/metadata.json"
        upload_ok = self.s3_uploader.upload_json(metadata, metadata_s3_key)
        if not upload_ok:
            return False, "Error uploading metadata to S3"

        return True, "File and metadata validated and uploaded successfully"