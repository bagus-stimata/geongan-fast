from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.fcompany import FCompany
from app.schemas.geongan.fcompany import FCompanyCreate


def create_fcompany(db: Session, company_in: FCompanyCreate):
    db_company = FCompany(**company_in.model_dump(by_alias=True))
    db.add(db_company)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_company)
    return db_company


def get_all_fcompany(db: Session):
    return db.query(FCompany).all()


def get_fcompany(db: Session, company_id: int):
    return db.query(FCompany).filter(FCompany.id == company_id).first()


def delete_fcompany(db: Session, company_id: int):
    db.query(FCompany).filter(FCompany.id == company_id).delete()
    db.commit()
