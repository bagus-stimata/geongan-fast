import importlib


def test_import_division_router():
    module = importlib.import_module("app.routers.geongan.division")
    assert hasattr(module, "router")
