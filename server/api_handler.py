from flask import Flask, request, jsonify
from flask_cors import CORS
from query_handler import QueryHandlerFactory
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
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

REQUEST_COUNT = Counter(
    "http_requests_total", "Total de solicitudes HTTP recibidas", ["method", "endpoint"]
)
REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds", "Latencia de las solicitudes HTTP", ["endpoint"]
)

def create_app(custom_query_handler=None):
    """Crea y configura una instancia de la aplicación Flask."""
    app = Flask(__name__)
    CORS(app)

    query_handler = custom_query_handler

    def handle_request(**kwargs):
        """Manejador genérico para las rutas."""
        endpoint = request.path
        method = request.method

        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()

        with REQUEST_LATENCY.labels(endpoint=endpoint).time():
            payload = {"route": request.path}
            response = query_handler.call(json.dumps(payload))
            return jsonify(json.loads(response))

    for route in routes:
        app.route(route, methods=["GET"])(handle_request)

    @app.route("/metrics")
    def metrics():
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    return app

if __name__ == '__main__':
    app = create_app(QueryHandlerFactory().create_query_handler("lambda"))
    app.run(debug=False)
