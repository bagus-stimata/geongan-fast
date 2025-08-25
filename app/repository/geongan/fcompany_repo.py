from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.fcompany import FCompany
from app.schemas.geongan.fcompany import FCompanyCreate

def create_fcompany(db: Session, fcompany_in: FCompanyCreate):
    db_fcompany = FCompany(**fcompany_in.model_dump())
    db.add(db_fcompany)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_fcompany)
    return db_fcompany


def get_all_fcompany(db: Session):
    return db.query(FCompany).all()


def get_fcompany(db: Session, fcompany_id: int):
    return db.query(FCompany).filter(FCompany.id == fcompany_id).first()


def delete_fcompany(db: Session, fcompany_id: int):
    db.query(FCompany).filter(FCompany.id == fcompany_id).delete()
    db.commit()
