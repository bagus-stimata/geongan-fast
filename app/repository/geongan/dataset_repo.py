from sqlalchemy.orm import Session

from app.models.dataset import Dataset
from app.schemas.geogan import DatasetCreate


def create_dataset(db: Session, dataset_in: DatasetCreate):
    db_dataset = Dataset(**dataset_in.model_dump())
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset


def get_all_dataset(db: Session):
    return db.query(Dataset).all()
