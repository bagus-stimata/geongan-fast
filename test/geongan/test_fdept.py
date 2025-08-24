import importlib

class TestFDept:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geongan.fdept")
        assert hasattr(module, "router")
