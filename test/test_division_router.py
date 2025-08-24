import importlib


def test_import_division_router():
    module = importlib.import_module("app.routers.division")
    assert hasattr(module, "router")
