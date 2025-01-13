from flask import Flask, request, jsonify
from flask_cors import CORS
from query_handler import QueryHandlerFactory

app = Flask(__name__)
query_handler = QueryHandlerFactory().create_query_handler("lambda")
CORS(app)

@app.route('/users', methods=['GET'])
def users():
    response = query_handler.call(request.data)
    return jsonify(response)

@app.route('/user/<string:user_id>', methods=['GET'])
def user(user_id):
    payload = {"user_name": user_id}
    response = query_handler.call(payload)
    return jsonify(response)

@app.route('/user/<string:user_id>/projects', methods=['GET'])
def user_projects(user_id):
    payload = {"user_name": user_id, "relationship": "OWNS"}
    response = query_handler.call(payload)
    return jsonify(response)

@app.route('/user/<string:user_id>/collaborations', methods=['GET'])
def user_collaborations(user_id):
    payload = {"user_name": user_id, "relationship": "COLLABORATES"}
    response = query_handler.call(payload)
    return jsonify(response)

@app.route('/user/<string:user_id>/collaborators', methods=['GET'])
def user_collaborators(user_id):
    payload = {"user_name": user_id, "relationship": "COLLABORATES"}
    response = query_handler.call(payload)
    return jsonify(response)

@app.route('/projects', methods=['GET'])
def projects():
    response = query_handler.call(request.data)
    return jsonify(response)

@app.route('/project/<string:project_id>', methods=['GET'])
def project(project_id):
    payload = {"project_name": project_id}
    response = query_handler.call(payload)
    return jsonify(response)

@app.route('/project/<string:project_id>/owner', methods=['GET'])
def project_owner(project_id):
    payload = {"project_name": project_id, "relationship": "OWNER"}
    response = query_handler.call(payload)
    return jsonify(response)

@app.route('/project/<string:project_id>/classes', methods=['GET'])
def project_classes(project_id):
    payload = {"project_name": project_id, "relationship": "CONTAINS"}
    response = query_handler.call(payload)
    return jsonify(response)

@app.route('/project/<string:project_id>/collaborators', methods=['GET'])
def project_collaborators(project_id):
    payload = {"project_name": project_id, "relationship": "COLLABORATES"}
    response = query_handler.call(payload)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)