from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.repository.geongan.link_resource_repo import (
    create_link_resource,
    get_all_link_resource,
)
from app.schemas.geongan.link_resource import (
    LinkResourceCreate,
    LinkResourceResponse,
)
from app.models.geongan.ft_link_resource import FtLinkResource


router = APIRouter(prefix="/api", tags=["link_resource"])


@router.post("/link-resources", response_model=LinkResourceResponse)
def create_link_resource_endpoint(
    payload: LinkResourceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    existing = db.query(FtLinkResource).filter_by(id=payload.id).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    result = create_link_resource(db, payload)
    return LinkResourceResponse.model_validate(result)


@router.get("/link-resources", response_model=list[LinkResourceResponse])
def read_all_link_resource(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    if "ROLE_ADMIN" not in current_user["roles"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin only")
    return get_all_link_resource(db)

