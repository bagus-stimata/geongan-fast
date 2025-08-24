from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geogan.ffiles_mutasi_repo import create_ffiles_mutasi, get_all_ffiles_mutasi
from app.schemas.geogan.ffiles_mutasi import FFilesMutasiCreate, FFilesMutasiResponse
from app.models.geogan.ffiles_mutasi import FFilesMutasi

router = APIRouter(prefix="/api/geogan", tags=["ffilesmutasi"])

@router.post("/createFFilesMutasi", response_model=FFilesMutasiResponse)
def create_ffiles_mutasi_endpoint(
    payload: FFilesMutasiCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FFilesMutasi).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_ffiles_mutasi(db, payload)
    return FFilesMutasiResponse.model_validate(result)

@router.get("/getAllFFilesMutasi", response_model=list[FFilesMutasiResponse])
def read_all_ffiles_mutasi(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_ffiles_mutasi(db)
