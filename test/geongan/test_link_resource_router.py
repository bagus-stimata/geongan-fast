import importlib


def test_import_link_resource_router():
    module = importlib.import_module("app.routers.geongan.link_resource")
    assert hasattr(module, "router")

