from httpx import AsyncClient, ASGITransport

from app.core.database import SessionLocal, Base, engine
from app.main import app
from app.routers.geongan import dataset_file as dataset_file_router
from app.core.security import create_access_token
from app.models.geongan.dataset import Dataset
from app.models.geongan.division import Division
from app.models.geongan.company import Company
import app.models as models  # ensure tables are registered

app.include_router(dataset_file_router.router)
import pytest


@pytest.mark.asyncio
async def test_create_dataset_file():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    db.add(Company(id=1, kode1="CMP", description="Test Company", status_active=True))
    db.add(Division(id=1, kode1="DIV", description="Test Division", company_id=1, status_active=True))
    db.add(Dataset(id=1, kode1="DS1", description="Dataset test", division_id=1, status_active=True))
    db.commit()
    db.close()

    token = create_access_token({
        "username": "test_user",
        "roles": ["ROLE_ADMIN"],
    })

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        headers = {"Authorization": f"Bearer {token}"}
        payload = {
            "id": 1,
            "dataset_id": 1,
            "file_name": "file.csv",
            "file_type": "csv",
            "jenis": "type",
            "flag": "flag",
            "description": "desc",
            "kode1": "FILE1",
        }
        response = await ac.post("/api/dataset-files", json=payload, headers=headers)
        assert response.status_code == 200

        response_get = await ac.get("/api/dataset-files", headers=headers)
        assert response_get.status_code == 200
        assert any(item["id"] == 1 for item in response_get.json())
