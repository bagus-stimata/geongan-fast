import importlib

class TestFFilesMutasi:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geongan.ffiles_mutasi")
        assert hasattr(module, "router")
