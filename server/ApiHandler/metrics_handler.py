from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

def metrics():
    """
    Expone las métricas de Prometheus en /metrics.
    """
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}