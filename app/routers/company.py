from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.company_repo import create_company, get_all_company
from app.schemas.company import CompanyCreate, CompanyResponse
from app.models.company import Company

router = APIRouter(prefix="/api", tags=["company"])


@router.post("/companies", response_model=CompanyResponse)
def create_company_endpoint(
    payload: CompanyCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(Company).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_company(db, payload)
    return CompanyResponse.model_validate(result)


@router.get("/companies", response_model=list[CompanyResponse])
def read_all_company(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_company(db)
