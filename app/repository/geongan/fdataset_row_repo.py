from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.fdataset_row import FDatasetRow
from app.schemas.geongan.fdataset_row import FDatasetRowCreate


def create_fdataset_row(db: Session, fdataset_row_in: FDatasetRowCreate):
    db_row = FDatasetRow(**fdataset_row_in.model_dump())
    db.add(db_row)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_row)
    return db_row


def get_all_fdataset_row(db: Session):
    return db.query(FDatasetRow).all()


def get_fdataset_row(db: Session, row_id: int):
    return db.query(FDatasetRow).filter(FDatasetRow.id == row_id).first()


def delete_fdataset_row(db: Session, row_id: int):
    db.query(FDatasetRow).filter(FDatasetRow.id == row_id).delete()
    db.commit()
