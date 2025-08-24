import importlib

class TestFCompany:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geogan.fcompany")
        assert hasattr(module, "router")
