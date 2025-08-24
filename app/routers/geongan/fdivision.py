from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.fdivision_repo import create_fdivision, get_all_fdivision
from app.schemas.geongan.fdivision import FDivisionCreate, FDivisionResponse
from app.models.geongan.fdivision import FDivision

router = APIRouter(prefix="/api/geongan", tags=["fdivision"])

@router.post("/createFDivision", response_model=FDivisionResponse)
def create_fdivision_endpoint(
    payload: FDivisionCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FDivision).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_fdivision(db, payload)
    return FDivisionResponse.model_validate(result)

@router.get("/getAllFDivision", response_model=list[FDivisionResponse])
def read_all_fdivision(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_fdivision(db)
