from httpx import AsyncClient, ASGITransport
import app.core.security as security
from app.core.database import SessionLocal, get_db
from app.main import app
from app.models.geongan.fcompany import FCompany
from app.routers.geongan import fcompany as fcompany_router
import pytest

# Configure security for tests
security.SECRET_KEY = "testsecret"
security.ALGORITHM = "HS256"
security.ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Override database dependency to use local SQLite

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Include the company router for testing
app.include_router(fcompany_router.router)

# Ensure the table exists
_db = SessionLocal()
FCompany.__table__.create(bind=_db.bind, checkfirst=True)
_db.close()


@pytest.mark.asyncio
async def test_create_fcompany():
    token = security.create_access_token({
        "username": "test_user",
        "roles": ["ROLE_ADMIN"],
    })

    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            headers = {"Authorization": f"Bearer {token}"}
            payload = {
                "id": 9991,
                "kode1": "CMP",
                "description": "Company Test",
                "status_active": True,
            }
            response = await ac.post("/api/fcompanies", json=payload, headers=headers)
            assert response.status_code == 200
    finally:
        db = SessionLocal()
        db.query(FCompany).filter(FCompany.id == 9991).delete()
        db.commit()
        db.close()


@pytest.mark.asyncio
async def test_get_fcompanies():
    token = security.create_access_token({
        "username": "test_user",
        "roles": ["ROLE_ADMIN"],
    })

    db = SessionLocal()
    db.query(FCompany).filter(FCompany.id == 9992).delete()
    dummy = FCompany(id=9992, kode1="CMP2", description="Dummy", status_active=True)
    db.add(dummy)
    db.commit()
    db.close()

    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            headers = {"Authorization": f"Bearer {token}"}
            response = await ac.get("/api/fcompanies", headers=headers)
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, list)
            assert any(item["id"] == 9992 for item in data)
    finally:
        db = SessionLocal()
        db.query(FCompany).filter(FCompany.id == 9992).delete()
        db.commit()
        db.close()
