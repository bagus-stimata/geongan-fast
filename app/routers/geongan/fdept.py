from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.fdept_repo import create_fdept, get_all_fdept
from app.schemas.geongan.fdept import FDeptCreate, FDeptResponse
from app.models.geongan.fdept import FDept

router = APIRouter(prefix="/api/geongan", tags=["fdept"])

@router.post("/createFDept", response_model=FDeptResponse)
def create_fdept_endpoint(
    payload: FDeptCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FDept).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_fdept(db, payload)
    return FDeptResponse.model_validate(result)

@router.get("/getAllFDept", response_model=list[FDeptResponse])
def read_all_fdept(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_fdept(db)
