from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.fproses_mutasi_repo import create_fproses_mutasi, get_all_fproses_mutasi
from app.schemas.geongan.fproses_mutasi import FProsesMutasiCreate, FProsesMutasiResponse
from app.models.geongan.fproses_mutasi import FProsesMutasi

router = APIRouter(prefix="/api/geongan", tags=["fprosesmutasi"])

@router.post("/createFProsesMutasi", response_model=FProsesMutasiResponse)
def create_fproses_mutasi_endpoint(
    payload: FProsesMutasiCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FProsesMutasi).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_fproses_mutasi(db, payload)
    return FProsesMutasiResponse.model_validate(result)

@router.get("/getAllFProsesMutasi", response_model=list[FProsesMutasiResponse])
def read_all_fproses_mutasi(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_fproses_mutasi(db)
