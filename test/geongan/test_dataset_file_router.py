import importlib


def test_import_dataset_file_router():
    module = importlib.import_module("app.routers.geongan.dataset_file")
    assert hasattr(module, "router")
