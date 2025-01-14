from flask import Flask, request, jsonify
from flask_cors import CORS
from query_handler import QueryHandlerFactory
import json

routes = [
    "/users",
    "/user/<string:user_id>",
    "/user/<string:user_id>/projects",
    "/user/<string:user_id>/collaborations",
    "/user/<string:user_id>/collaborators",
    "/projects",
    "/project/<string:project_id>",
    "/project/<string:project_id>/owner",
    "/project/<string:project_id>/classes",
    "/project/<string:project_id>/collaborators",
]

def create_app(custom_query_handler=None):
    """Crea y configura una instancia de la aplicación Flask."""
    app = Flask(__name__)
    CORS(app)

    query_handler = custom_query_handler

    def handle_request(**kwargs):
        """Manejador genérico para las rutas."""
        payload = {"route": request.path}
        response = query_handler.call(json.dumps(payload))
        return jsonify(json.loads(response))

    for route in routes:
        app.route(route, methods=["GET"])(handle_request)

    return app

if __name__ == '__main__':
    app = create_app(QueryHandlerFactory().create_query_handler("lambda"))
    app.run(debug=False)