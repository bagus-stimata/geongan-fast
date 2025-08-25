from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.fdataset_row_repo import (
    create_fdataset_row,
    get_all_fdataset_row,
)
from app.schemas.geongan.fdataset_row import FDatasetRowCreate, FDatasetRowResponse
from app.models.geongan.fdataset_row import FDatasetRow

router = APIRouter(prefix="/api", tags=["fdataset_row"])


@router.post("/fdataset-rows", response_model=FDatasetRowResponse)
def create_fdataset_row_endpoint(
    payload: FDatasetRowCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FDatasetRow).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_fdataset_row(db, payload)
    return FDatasetRowResponse.model_validate(result)


@router.get("/fdataset-rows", response_model=list[FDatasetRowResponse])
def read_all_fdataset_row(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_fdataset_row(db)
