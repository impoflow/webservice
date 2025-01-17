import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from services.validation_service import ValidationService
from services.s3_uploader import S3Uploader
from builders.file_upload_builder import FileUploadBuilder

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"zip"}

app = Flask(__name__)
CORS(app)

S3_BUCKET_NAME = "neo4j-tscd-310-10-2025"
AWS_REGION = "us-east-1"

validation_service = ValidationService()
s3_uploader = S3Uploader(bucket_name=S3_BUCKET_NAME, aws_region=AWS_REGION)

def allowed_file(filename: str) -> bool:
    """
    Verifica si el archivo tiene una extensión permitida.
    """
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@app.route("/upload", methods=["POST"])
def handle_upload():
    """
    Maneja la carga de archivos ZIP:
     - Valida campos requeridos.
     - Guarda temporalmente el archivo.
     - Construye y ejecuta el proceso de validación y subida a S3.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]
    if not file or file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    user_name = request.form.get("user_name")
    collaborators_raw = request.form.get("collaborators", "")

    if not user_name:
        return jsonify({"error": "Missing required fields: user_name"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    collaborators = [c.strip() for c in collaborators_raw.split(",")] if collaborators_raw else []
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    try:
        upload_manager = (
            FileUploadBuilder()
            .with_file_path(file_path)
            .with_user_name(user_name)
            .with_project_name(file.filename.rsplit(".", 1)[0])
            .with_collaborators(collaborators)
            .with_validation_service(validation_service)
            .with_s3_uploader(s3_uploader)
            .build()
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    is_success, message = upload_manager.validate_and_upload()

    if not is_success:
        return jsonify({"error": message}), 400

    response_data = {
        "message": message,
        "user_name": user_name,
        "project_name": file.filename,
        "collaborators": collaborators
    }
    return jsonify(response_data), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)