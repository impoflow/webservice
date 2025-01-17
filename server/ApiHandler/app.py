from flask import Flask
from flask_cors import CORS

from services.query_handler_factory import QueryHandlerFactory
from route_manager import RouteManager
from metrics_handler import metrics


def create_app(query_handler_type="lambda"):
    """
    Crea y configura la aplicación Flask, registrando rutas y métricas.
    """
    app = Flask(__name__)
    CORS(app)

    query_handler = QueryHandlerFactory().create_query_handler(query_handler_type)

    route_manager = RouteManager(app, query_handler)
    route_manager.register_routes()

    app.add_url_rule("/metrics", "metrics", metrics, methods=["GET"])
    app.add_url_rule("/health", "health", lambda: "OK", methods=["GET"])

    return app


if __name__ == "__main__":
    app = create_app(query_handler_type="lambda")
    app.run(host="0.0.0.0", port=5000, debug=False)
