import importlib


def test_import_endpoint_access_router():
    module = importlib.import_module("app.routers.geongan.endpoint_access")
    assert hasattr(module, "router")

