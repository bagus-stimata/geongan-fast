from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geogan.fstatus_mutasi_repo import create_fstatus_mutasi, get_all_fstatus_mutasi
from app.schemas.geogan.fstatus_mutasi import FStatusMutasiCreate, FStatusMutasiResponse
from app.models.geogan.fstatus_mutasi import FStatusMutasi

router = APIRouter(prefix="/api/geogan", tags=["fstatusmutasi"])

@router.post("/createFStatusMutasi", response_model=FStatusMutasiResponse)
def create_fstatus_mutasi_endpoint(
    payload: FStatusMutasiCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FStatusMutasi).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_fstatus_mutasi(db, payload)
    return FStatusMutasiResponse.model_validate(result)

@router.get("/getAllFStatusMutasi", response_model=list[FStatusMutasiResponse])
def read_all_fstatus_mutasi(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_fstatus_mutasi(db)
