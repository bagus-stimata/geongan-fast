from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.geogan.company import CompanyCreate


def create_company(db: Session, company_in: CompanyCreate):
    db_company = Company(**company_in.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def get_all_company(db: Session):
    return db.query(Company).all()
