import importlib


def test_import_dataset_router():
    module = importlib.import_module("app.routers.dataset")
    assert hasattr(module, "router")
