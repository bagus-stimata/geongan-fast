from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.ft_link_resource import FtLinkResource
from app.schemas.geongan.ft_link_resource import FtLinkResourceCreate


def create_ft_link_resource(db: Session, ft_link_resource_in: FtLinkResourceCreate):
    db_obj = FtLinkResource(**ft_link_resource_in.model_dump())
    db.add(db_obj)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_obj)
    return db_obj


def get_all_ft_link_resource(db: Session):
    return db.query(FtLinkResource).all()


def get_ft_link_resource(db: Session, link_id: int):
    return db.query(FtLinkResource).filter(FtLinkResource.id == link_id).first()


def delete_ft_link_resource(db: Session, link_id: int):
    db.query(FtLinkResource).filter(FtLinkResource.id == link_id).delete()
    db.commit()

