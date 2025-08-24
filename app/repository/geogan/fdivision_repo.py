from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geogan.fdivision import FDivision
from app.schemas.geogan.fdivision import FDivisionCreate


def create_fdivision(db: Session, division_in: FDivisionCreate):
    db_division = FDivision(**division_in.model_dump(by_alias=True))
    db.add(db_division)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_division)
    return db_division


def get_all_fdivision(db: Session):
    return db.query(FDivision).all()


def get_fdivision(db: Session, division_id: int):
    return db.query(FDivision).filter(FDivision.id == division_id).first()


def delete_fdivision(db: Session, division_id: int):
    db.query(FDivision).filter(FDivision.id == division_id).delete()
    db.commit()
