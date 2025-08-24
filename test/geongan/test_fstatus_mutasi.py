import importlib

class TestFStatusMutasi:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geongan.fstatus_mutasi")
        assert hasattr(module, "router")
