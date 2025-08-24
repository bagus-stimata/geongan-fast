import importlib

class TestFFilesMutasi:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geogan.ffiles_mutasi")
        assert hasattr(module, "router")
