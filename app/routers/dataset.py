from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.dataset_repo import create_dataset, get_all_dataset
from app.schemas.dataset import DatasetCreate, DatasetResponse
from app.models.dataset import Dataset

router = APIRouter(prefix="/api", tags=["dataset"])


@router.post("/datasets", response_model=DatasetResponse)
def create_dataset_endpoint(
    payload: DatasetCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(Dataset).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_dataset(db, payload)
    return DatasetResponse.model_validate(result)


@router.get("/datasets", response_model=list[DatasetResponse])
def read_all_dataset(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_dataset(db)
