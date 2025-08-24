from sqlalchemy.orm import Session

from app.models.geongan.ft_endpoint_access import FtEndpointAccess
from app.schemas.geongan.endpoint_access import EndpointAccessCreate


def create_endpoint_access(db: Session, endpoint_access_in: EndpointAccessCreate):
    db_obj = FtEndpointAccess(**endpoint_access_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_all_endpoint_access(db: Session):
    return db.query(FtEndpointAccess).all()


def get_endpoint_access(db: Session, access_id: int):
    return db.query(FtEndpointAccess).filter(FtEndpointAccess.id == access_id).first()


def delete_endpoint_access(db: Session, access_id: int):
    db.query(FtEndpointAccess).filter(FtEndpointAccess.id == access_id).delete()
    db.commit()

