import importlib

class TestFDivision:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geogan.fdivision")
        assert hasattr(module, "router")
