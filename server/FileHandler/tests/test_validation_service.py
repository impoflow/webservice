import unittest
import zipfile
import os
from services.validation_service import ValidationService

class TestValidationService(unittest.TestCase):
    def setUp(self):
        self.validation_service = ValidationService()
        self.temp_files = []  # Lista para rastrear archivos temporales creados

    def tearDown(self):
        for file_path in getattr(self, "temp_files", []):
            if os.path.isfile(file_path):  # Verifica que sea un archivo
                os.remove(file_path)
            elif os.path.isdir(file_path):  # Solo para asegurarte, si es un directorio
                print(f"Skipping directory: {file_path}")

    def test_validate_zip_file_no_java_files(self):
        with zipfile.ZipFile("test.zip", "w") as zf:
            zf.writestr("file.txt", "This is a text file")
        self.temp_files.append("test.zip")  # Rastrear el archivo creado

        is_valid, message = self.validation_service.validate_zip_file("test.zip")
        self.assertFalse(is_valid)
        self.assertEqual(message, "No .java files found in the ZIP file")

    def test_validate_zip_file_no_main(self):
        with zipfile.ZipFile("test.zip", "w") as zf:
            zf.writestr("Test.java", "class Test {}")
        self.temp_files.append("test.zip")  # Rastrear el archivo creado

        is_valid, message = self.validation_service.validate_zip_file("test.zip")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Error: 'public static void main' not found in the content")

    def test_validate_zip_file_multiple_mains(self):
        content = """
        public class Test {
            public static void main(String[] args) {}
        }
        public class AnotherTest {
            public static void main(String[] args) {}
        }
        """
        with zipfile.ZipFile("test.zip", "w") as zf:
            zf.writestr("Test.java", content)
        self.temp_files.append("test.zip")  # Rastrear el archivo creado

        is_valid, message = self.validation_service.validate_zip_file("test.zip")
        self.assertFalse(is_valid)
        self.assertEqual(message, "Error: More than one 'public static void main' found")

    def test_validate_zip_file_success(self):
        content = """
        public class Test {
            public static void main(String[] args) {}
        }
        """
        with zipfile.ZipFile("test.zip", "w") as zf:
            zf.writestr("Test.java", content)
        self.temp_files.append("test.zip")  # Rastrear el archivo creado

        is_valid, message = self.validation_service.validate_zip_file("test.zip")
        self.assertTrue(is_valid)
        self.assertEqual(message, "Validation successful")

if __name__ == "__main__":
    unittest.main()
