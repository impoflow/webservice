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
    "http_requests_total", "Total HTTP requests received", ["method", "endpoint"]
)
REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds", "Latency of HTTP requests", ["endpoint"]
)

def handle_request(query_handler, endpoint):
    """Handles requests for a specific route."""
    method = request.method

    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()

    with REQUEST_LATENCY.labels(endpoint=endpoint).time():
        payload = {"route": endpoint}
        response = query_handler.call(json.dumps(payload))
        return jsonify(json.loads(response))

def create_view_func(query_handler, route):
    """Creates a view function for a specific route."""
    def view_func(**kwargs):
        return handle_request(query_handler, route)
    return view_func

def register_routes(app, query_handler):
    """Registers all defined routes in the Flask app."""
    for route in routes:
        app.add_url_rule(
            route,
            endpoint=route,
            view_func=create_view_func(query_handler, route),
            methods=["GET"],
        )

def metrics():
    """Exposes Prometheus metrics."""
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

def create_app(custom_query_handler=None):
    """Creates and configures the Flask application."""
    app = Flask(__name__)
    CORS(app)

    query_handler = custom_query_handler or QueryHandlerFactory().create_query_handler("lambda")

    register_routes(app, query_handler)
    app.add_url_rule("/metrics", "metrics", metrics, methods=["GET"])

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)
