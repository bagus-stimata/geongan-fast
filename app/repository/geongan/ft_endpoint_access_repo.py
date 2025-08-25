from sqlalchemy.orm import Session

from app.models.geongan.ft_endpoint_access import FtEndpointAccess
from app.schemas.geongan.ft_endpoint_access import FtEndpointAccessCreate


def create_ft_endpoint_access(
    db: Session, ft_endpoint_access_in: FtEndpointAccessCreate
):
    db_obj = FtEndpointAccess(**ft_endpoint_access_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_all_ft_endpoint_access(db: Session):
    return db.query(FtEndpointAccess).all()


def get_ft_endpoint_access(db: Session, access_id: int):
    return db.query(FtEndpointAccess).filter(FtEndpointAccess.id == access_id).first()


def delete_ft_endpoint_access(db: Session, access_id: int):
    db.query(FtEndpointAccess).filter(FtEndpointAccess.id == access_id).delete()
    db.commit()

