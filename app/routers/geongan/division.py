from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.division_repo import create_division, get_all_division
from app.schemas.geogan import DivisionCreate, DivisionResponse
from app.models.division import Division

router = APIRouter(prefix="/api", tags=["division"])


@router.post("/divisions", response_model=DivisionResponse)
def create_division_endpoint(
    payload: DivisionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(Division).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_division(db, payload)
    return DivisionResponse.model_validate(result)


@router.get("/divisions", response_model=list[DivisionResponse])
def read_all_division(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_division(db)
