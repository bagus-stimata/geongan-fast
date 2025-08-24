from sqlalchemy.orm import Session

from app.models.dataset_file import DatasetFile
from app.schemas.geongan.dataset_file import DatasetFileCreate


def create_dataset_file(db: Session, dataset_file_in: DatasetFileCreate):
    db_file = DatasetFile(**dataset_file_in.model_dump())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


def get_all_dataset_file(db: Session):
    return db.query(DatasetFile).all()
