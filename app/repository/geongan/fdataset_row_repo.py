from sqlalchemy.orm import Session

from app.models.geongan.fdataset_row import FDatasetRow
from app.schemas.geongan.fdataset_row import FDatasetRowCreate


def create_fdataset_row(db: Session, fdataset_row_in: FDatasetRowCreate):
    db_row = FDatasetRow(**fdataset_row_in.model_dump())
    db.add(db_row)
    db.commit()
    db.refresh(db_row)
    return db_row


def get_all_fdataset_row(db: Session):
    return db.query(FDatasetRow).all()
