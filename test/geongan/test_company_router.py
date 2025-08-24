import importlib


def test_import_company_router():
    module = importlib.import_module("app.routers.company")
    assert hasattr(module, "router")
