from flask import request, jsonify
from prometheus_client import Counter, Histogram
import json

from api_routes import ROUTES


REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests received",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "Latency of HTTP requests",
    ["endpoint"]
)


class RouteManager:
    """
    Se encarga de registrar las rutas y manejar la lógica de cada petición.
    """

    def __init__(self, app, query_handler):
        self.app = app
        self.query_handler = query_handler

    def register_routes(self):
        """
        Registra todas las rutas definidas en api_routes.ROUTES.
        """
        for route in ROUTES:
            self.app.add_url_rule(
                route,
                endpoint=route,
                view_func=self._create_view_func(route),
                methods=["GET"]
            )

    def _create_view_func(self, route):
        """
        Crea la función de vista (view_func) para cada ruta.
        """
        def view_func(**kwargs):
            return self._handle_request(route)
        return view_func

    def _handle_request(self, endpoint):
        """
        Maneja la petición entrante, registra métricas,
        e invoca la lógica apropiada del QueryHandler.
        """
        method = request.method
        REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()

        with REQUEST_LATENCY.labels(endpoint=endpoint).time():
            payload = {"route": endpoint}

            response_data = self.query_handler.call(json.dumps(payload))
            return jsonify(json.loads(response_data))
