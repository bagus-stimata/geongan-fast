from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.ft_link_resource_repo import (
    create_ft_link_resource,
    get_all_ft_link_resource,
)
from app.schemas.geongan.ft_link_resource import (
    FtLinkResourceCreate,
    FtLinkResourceResponse,
)
from app.models.geongan.ft_link_resource import FtLinkResource


router = APIRouter(prefix="/api", tags=["ft_link_resource"])


@router.post("/ft-link-resources", response_model=FtLinkResourceResponse)
def create_ft_link_resource_endpoint(
    payload: FtLinkResourceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FtLinkResource).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_ft_link_resource(db, payload)
    return FtLinkResourceResponse.model_validate(result)


@router.get("/ft-link-resources", response_model=list[FtLinkResourceResponse])
def read_all_ft_link_resource(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_ft_link_resource(db)

