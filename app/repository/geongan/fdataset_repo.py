from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.fdataset import FDataset
from app.schemas.geongan.fdataset import FDatasetCreate


def create_fdataset(db: Session, fdataset_in: FDatasetCreate):
    db_fdataset = FDataset(**fdataset_in.model_dump())
    db.add(db_fdataset)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_fdataset)
    return db_fdataset


def get_all_fdataset(db: Session):
    return db.query(FDataset).all()


def get_fdataset(db: Session, dataset_id: int):
    return db.query(FDataset).filter(FDataset.id == dataset_id).first()


def delete_fdataset(db: Session, dataset_id: int):
    db.query(FDataset).filter(FDataset.id == dataset_id).delete()
    db.commit()
