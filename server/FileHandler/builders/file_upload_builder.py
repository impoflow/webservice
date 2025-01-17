from services.file_upload_manager import FileUploadManager

class FileUploadBuilder:
    """
    Implementación del patrón Builder para construir un FileUploadManager
    con toda la información necesaria para validar y subir un archivo.
    """

    def __init__(self):
        self._file_path = None
        self._user_name = None
        self._project_name = None
        self._collaborators = []
        self._validation_service = None
        self._s3_uploader = None

    def with_file_path(self, file_path: str):
        self._file_path = file_path
        return self

    def with_user_name(self, user_name: str):
        self._user_name = user_name
        return self

    def with_project_name(self, project_name: str):
        self._project_name = project_name
        return self

    def with_collaborators(self, collaborators: list[str]):
        self._collaborators = collaborators
        return self

    def with_validation_service(self, validation_service):
        self._validation_service = validation_service
        return self

    def with_s3_uploader(self, s3_uploader):
        self._s3_uploader = s3_uploader
        return self

    def build(self) -> FileUploadManager:
        """
        Retorna una instancia de FileUploadManager debidamente configurada.
        """
        if not all([
            self._file_path, 
            self._user_name, 
            self._project_name,
            self._validation_service,
            self._s3_uploader
        ]):
            raise ValueError("Missing required fields or services for file upload builder")

        return FileUploadManager(
            file_path=self._file_path,
            user_name=self._user_name,
            project_name=self._project_name,
            collaborators=self._collaborators,
            validation_service=self._validation_service,
            s3_uploader=self._s3_uploader
        )