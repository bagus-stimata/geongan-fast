from sqlalchemy.orm import Session

from app.models.geongan.fdataset_file import FDatasetFille
from app.schemas.geongan.fdataset_file import FDatasetFileCreate


def create_fdataset_file(db: Session, fdataset_file_in: FDatasetFileCreate):
    db_file = FDatasetFille(**fdataset_file_in.model_dump())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file


def get_all_fdataset_file(db: Session):
    return db.query(FDatasetFille).all()
