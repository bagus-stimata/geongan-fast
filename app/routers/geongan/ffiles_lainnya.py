from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.ffiles_lainnya_repo import create_ffiles_lainnya, get_all_ffiles_lainnya
from app.schemas.geongan.ffiles_lainnya import FFilesLainnyaCreate, FFilesLainnyaResponse
from app.models.geongan.ffiles_lainnya import FFilesLainnya

router = APIRouter(prefix="/api/geongan", tags=["ffileslainnya"])

@router.post("/createFFilesLainnya", response_model=FFilesLainnyaResponse)
def create_ffiles_lainnya_endpoint(
    payload: FFilesLainnyaCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FFilesLainnya).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_ffiles_lainnya(db, payload)
    return FFilesLainnyaResponse.model_validate(result)

@router.get("/getAllFFilesLainnya", response_model=list[FFilesLainnyaResponse])
def read_all_ffiles_lainnya(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_ffiles_lainnya(db)
