from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.dataset_row_repo import create_dataset_row, get_all_dataset_row
from app.schemas.geongan.dataset_row import DatasetRowCreate, DatasetRowResponse
from app.models.geongan.dataset_row import DatasetRow

router = APIRouter(prefix="/api", tags=["dataset_row"])


@router.post("/dataset-rows", response_model=DatasetRowResponse)
def create_dataset_row_endpoint(
    payload: DatasetRowCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(DatasetRow).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_dataset_row(db, payload)
    return DatasetRowResponse.model_validate(result)


@router.get("/dataset-rows", response_model=list[DatasetRowResponse])
def read_all_dataset_row(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_dataset_row(db)
