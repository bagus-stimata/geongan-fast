from sqlalchemy.orm import Session

from app.models.geongan.fcompany import FCompany
from app.schemas.geongan.company import CompanyCreate


def create_company(db: Session, company_in: CompanyCreate):
    db_company = FCompany(**company_in.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def get_all_company(db: Session):
    return db.query(FCompany).all()
