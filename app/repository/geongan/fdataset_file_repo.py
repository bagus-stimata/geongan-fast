from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.fdataset_file import FDatasetFille
from app.schemas.geongan.fdataset_file import FDatasetFileCreate


def create_fdataset_file(db: Session, fdataset_file_in: FDatasetFileCreate):
    db_file = FDatasetFille(**fdataset_file_in.model_dump())
    db.add(db_file)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_file)
    return db_file


def get_all_fdataset_file(db: Session):
    return db.query(FDatasetFille).all()


def get_fdataset_file(db: Session, file_id: int):
    return db.query(FDatasetFille).filter(FDatasetFille.id == file_id).first()


def delete_fdataset_file(db: Session, file_id: int):
    db.query(FDatasetFille).filter(FDatasetFille.id == file_id).delete()
    db.commit()
