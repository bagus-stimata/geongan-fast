from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.ft_endpoint_access_repo import (
    create_ft_endpoint_access,
    get_all_ft_endpoint_access,
)
from app.schemas.geongan.ft_endpoint_access import (
    FtEndpointAccessCreate,
    FtEndpointAccessResponse,
)
from app.models.geongan.ft_endpoint_access import FtEndpointAccess


router = APIRouter(prefix="/api", tags=["ft_endpoint_access"])


@router.post("/ft-endpoint-accesses", response_model=FtEndpointAccessResponse)
def create_ft_endpoint_access_endpoint(
    payload: FtEndpointAccessCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FtEndpointAccess).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_ft_endpoint_access(db, payload)
    return FtEndpointAccessResponse.model_validate(result)


@router.get(
    "/ft-endpoint-accesses", response_model=list[FtEndpointAccessResponse]
)
def read_all_ft_endpoint_access(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_ft_endpoint_access(db)

