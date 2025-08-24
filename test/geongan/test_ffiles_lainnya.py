import importlib

class TestFFilesLainnya:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geogan.ffiles_lainnya")
        assert hasattr(module, "router")
