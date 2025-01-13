from flask import Flask, request, jsonify
from flask_cors import CORS
from query_handler import QueryHandlerFactory
import json

app = Flask(__name__)
query_handler = QueryHandlerFactory().create_query_handler("lambda")
CORS(app)

@app.route('/users', methods=['GET'])
def users():
    payload = request.get_json() or {}  # Asegura que el payload no sea None
    payload_bytes = json.dumps(payload).encode('utf-8')  # Serializa a bytes
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))  # Decodifica la respuesta para enviar JSON

@app.route('/user/<string:user_id>', methods=['GET'])
def user(user_id):
    payload = {"user_name": user_id}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/user/<string:user_id>/projects', methods=['GET'])
def user_projects(user_id):
    payload = {"user_name": user_id, "relationship": "OWNS"}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/user/<string:user_id>/collaborations', methods=['GET'])
def user_collaborations(user_id):
    payload = {"user_name": user_id, "relationship": "COLLABORATES"}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/user/<string:user_id>/collaborators', methods=['GET'])
def user_collaborators(user_id):
    payload = {"user_name": user_id, "relationship": "COLLABORATES"}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/projects', methods=['GET'])
def projects():
    payload = request.get_json() or {}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/project/<string:project_id>', methods=['GET'])
def project(project_id):
    payload = {"project_name": project_id}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/project/<string:project_id>/owner', methods=['GET'])
def project_owner(project_id):
    payload = {"project_name": project_id, "relationship": "OWNER"}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/project/<string:project_id>/classes', methods=['GET'])
def project_classes(project_id):
    payload = {"project_name": project_id, "relationship": "CONTAINS"}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

@app.route('/project/<string:project_id>/collaborators', methods=['GET'])
def project_collaborators(project_id):
    payload = {"project_name": project_id, "relationship": "COLLABORATES"}
    payload_bytes = json.dumps(payload).encode('utf-8')
    response = query_handler.call(payload_bytes)
    return jsonify(json.loads(response))

if __name__ == '__main__':
    app.run(debug=False)
