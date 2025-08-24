from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.fdatabase_repo import create_fdatabase, get_all_fdatabase
from app.schemas.geongan.fdatabase import FDatabaseCreate, FDatabaseResponse
from app.models.geongan.fdatabase import FDatabase

router = APIRouter(prefix="/api/geongan", tags=["fdatabase"])

@router.post("/createFDatabase", response_model=FDatabaseResponse)
def create_fdatabase_endpoint(
    payload: FDatabaseCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FDatabase).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_fdatabase(db, payload)
    return FDatabaseResponse.model_validate(result)

@router.get("/getAllFDatabase", response_model=list[FDatabaseResponse])
def read_all_fdatabase(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_fdatabase(db)
