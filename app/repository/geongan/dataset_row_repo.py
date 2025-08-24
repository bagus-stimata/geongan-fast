from sqlalchemy.orm import Session

from app.models.geongan.fdataset_row import FDatasetRow
from app.schemas.geongan.dataset_row import DatasetRowCreate


def create_dataset_row(db: Session, dataset_row_in: DatasetRowCreate):
    db_row = FDatasetRow(**dataset_row_in.model_dump())
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row


def get_all_dataset_row(db: Session):
    return db.query(FDatasetRow).all()
