from httpx import AsyncClient, ASGITransport
import app.core.security as security
from app.core.database import SessionLocal, get_db
from app.main import app
from app.models.geongan.company import Company
from app.models.geongan.division import Division
from app.routers.geongan import company as company_router
from app.routers.geongan import division as division_router
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

# Include routers for testing
app.include_router(company_router.router)
app.include_router(division_router.router)

# Ensure the tables exist
_db = SessionLocal()
Company.__table__.create(bind=_db.bind, checkfirst=True)
Division.__table__.create(bind=_db.bind, checkfirst=True)
_db.close()


@pytest.mark.asyncio
async def test_create_division():
    db = SessionLocal()
    db.query(Division).filter(Division.id == 9994).delete()
    db.query(Company).filter(Company.id == 9993).delete()
    dummy_company = Company(id=9993, kode1="CMP3", description="Company for division", status_active=True)
    db.add(dummy_company)
    db.commit()
    db.close()

    token = security.create_access_token({
        "username": "test_user",
        "roles": ["ROLE_ADMIN"],
    })

    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            headers = {"Authorization": f"Bearer {token}"}
            payload = {
                "id": 9994,
                "kode1": "DIV",
                "description": "Division Test",
                "company_id": 9993,
                "status_active": True,
            }
            response = await ac.post("/api/divisions", json=payload, headers=headers)
            assert response.status_code == 200
    finally:
        db = SessionLocal()
        db.query(Division).filter(Division.id == 9994).delete()
        db.query(Company).filter(Company.id == 9993).delete()
        db.commit()
        db.close()


@pytest.mark.asyncio
async def test_get_divisions():
    db = SessionLocal()
    db.query(Division).filter(Division.id == 9996).delete()
    db.query(Company).filter(Company.id == 9995).delete()
    dummy_company = Company(id=9995, kode1="CMP4", description="Dummy Co", status_active=True)
    dummy_division = Division(id=9996, kode1="DIV2", description="Dummy Div", company_id=9995, status_active=True)
    db.add(dummy_company)
    db.add(dummy_division)
    db.commit()
    db.close()

    token = security.create_access_token({
        "username": "test_user",
        "roles": ["ROLE_ADMIN"],
    })

    try:
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            headers = {"Authorization": f"Bearer {token}"}
            response = await ac.get("/api/divisions", headers=headers)
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, list)
            assert any(item["id"] == 9996 for item in data)
    finally:
        db = SessionLocal()
        db.query(Division).filter(Division.id == 9996).delete()
        db.query(Company).filter(Company.id == 9995).delete()
        db.commit()
        db.close()
