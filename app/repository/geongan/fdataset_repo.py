from sqlalchemy.orm import Session

from app.models.geongan.fdataset import FDataset
from app.schemas.geongan.dataset import DatasetCreate


def create_dataset(db: Session, dataset_in: DatasetCreate):
    db_dataset = FDataset(**dataset_in.model_dump())
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset


def get_all_dataset(db: Session):
    return db.query(FDataset).all()
