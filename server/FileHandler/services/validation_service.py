import zipfile

class ValidationService:
    """
    Servicio responsable de validar los archivos ZIP.
    """
    def validate_zip_file(self, zip_file_path: str) -> tuple[bool, str]:
        """
        Valida el contenido de un archivo ZIP:
          - Debe contener al menos un archivo .java.
          - Debe tener exactamente una definición de 'public static void main'.
        Retorna (is_valid, message).
        """
        try:
            with zipfile.ZipFile(zip_file_path, "r") as zf:
                java_files = []
                full_content = ""

                for file_info in zf.infolist():
                    if file_info.filename.endswith(".java"):
                        java_files.append(file_info.filename)
                        with zf.open(file_info.filename) as java_file:
                            full_content += java_file.read().decode("utf-8")

                if not java_files:
                    return False, "No .java files found in the ZIP file"

                main_count = full_content.count("public static void main")
                if main_count == 0:
                    return False, "Error: 'public static void main' not found in the content"
                if main_count > 1:
                    return False, "Error: More than one 'public static void main' found"

                return True, "Validation successful"

        except zipfile.BadZipFile:
            return False, "Uploaded file is not a valid ZIP file"