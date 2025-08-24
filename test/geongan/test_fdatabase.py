import importlib

class TestFDatabase:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geogan.fdatabase")
        assert hasattr(module, "router")
