import importlib

class TestFProsesMutasi:
    def test_import_router(self):
        module = importlib.import_module("app.routers.geongan.fproses_mutasi")
        assert hasattr(module, "router")
