from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.ft_endpoint_access_repo import (
    create_endpoint_access,
    get_all_endpoint_access,
)
from app.schemas.geongan.endpoint_access import (
    EndpointAccessCreate,
    EndpointAccessResponse,
)
from app.models.geongan.ft_endpoint_access import FtEndpointAccess


router = APIRouter(prefix="/api", tags=["endpoint_access"])


@router.post("/endpoint-accesses", response_model=EndpointAccessResponse)
def create_endpoint_access_endpoint(
    payload: EndpointAccessCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FtEndpointAccess).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_endpoint_access(db, payload)
    return EndpointAccessResponse.model_validate(result)


@router.get("/endpoint-accesses", response_model=list[EndpointAccessResponse])
def read_all_endpoint_access(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_endpoint_access(db)

