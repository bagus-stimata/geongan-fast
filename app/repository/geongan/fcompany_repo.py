from sqlalchemy.orm import Session

from app.models.geongan.fcompany import FCompany
from app.schemas.geongan.fcompany import FCompanyCreate

def create_fcompany(db: Session, fcompany_in: FCompanyCreate):
    db_fcompany = FCompany(**fcompany_in.model_dump())
    db.add(db_fcompany)
    db.commit()
    db.refresh(db_fcompany)
    return db_fcompany


def get_all_fcompany(db: Session):
    return db.query(FCompany).all()
