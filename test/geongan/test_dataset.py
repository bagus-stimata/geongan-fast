from httpx import AsyncClient, ASGITransport

from app.core.database import SessionLocal, Base, engine
from app.main import app
from app.routers.geongan import dataset as dataset_router
from app.core.security import create_access_token
from app.models.geongan.division import Division
from app.models.geongan.company import Company
import app.models as models  # ensure tables are registered

app.include_router(dataset_router.router)
import pytest


@pytest.mark.asyncio
async def test_create_dataset():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    db.add(Company(id=1, kode1="CMP", description="Test Company", status_active=True))
    db.add(Division(id=1, kode1="DIV", description="Test Division", company_id=1, status_active=True))
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
            "kode1": "DS1",
            "description": "Dataset test",
            "division_id": 1,
            "status_active": True,
        }
        response = await ac.post("/api/datasets", json=payload, headers=headers)
        assert response.status_code == 200

        response_get = await ac.get("/api/datasets", headers=headers)
        assert response_get.status_code == 200
        assert any(item["id"] == 1 for item in response_get.json())
