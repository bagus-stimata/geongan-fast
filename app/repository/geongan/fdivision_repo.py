from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.fdivision import FDivision
from app.schemas.geongan.fdivision import FDivisionCreate


def create_fdivision(db: Session, fdivision_in: FDivisionCreate):
    db_fdivision = FDivision(**fdivision_in.model_dump())
    db.add(db_fdivision)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_fdivision)
    return db_fdivision


def get_all_fdivision(db: Session):
    return db.query(FDivision).all()


def get_fdivision(db: Session, division_id: int):
    return db.query(FDivision).filter(FDivision.id == division_id).first()


def delete_fdivision(db: Session, division_id: int):
    db.query(FDivision).filter(FDivision.id == division_id).delete()
    db.commit()
