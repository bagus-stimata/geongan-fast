from sqlalchemy.orm import Session

from app.models.geongan.fdataset import FDataset
from app.schemas.geongan.fdataset import FDatasetCreate


def create_fdataset(db: Session, fdataset_in: FDatasetCreate):
    db_fdataset = FDataset(**fdataset_in.model_dump())
    db.add(db_fdataset)
    db.commit()
    db.refresh(db_fdataset)
    return db_fdataset


def get_all_fdataset(db: Session):
    return db.query(FDataset).all()
