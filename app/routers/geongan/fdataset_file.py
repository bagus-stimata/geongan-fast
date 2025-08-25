from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.fdataset_file_repo import (
    create_fdataset_file,
    get_all_fdataset_file,
)
from app.schemas.geongan.fdataset_file import FDatasetFileCreate, FDatasetFileResponse
from app.models.geongan.fdataset_file import FDatasetFille

router = APIRouter(prefix="/api", tags=["fdataset_file"])


@router.post("/fdataset-files", response_model=FDatasetFileResponse)
def create_fdataset_file_endpoint(
    payload: FDatasetFileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FDatasetFille).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_fdataset_file(db, payload)
    return FDatasetFileResponse.model_validate(result)


@router.get("/fdataset-files", response_model=list[FDatasetFileResponse])
def read_all_fdataset_file(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_fdataset_file(db)
