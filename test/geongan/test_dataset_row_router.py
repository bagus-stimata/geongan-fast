import importlib


def test_import_dataset_row_router():
    module = importlib.import_module("app.routers.geongan.dataset_row")
    assert hasattr(module, "router")
