from sqlalchemy.orm import Session

from app.models.geongan.fdivision import FDivision
from app.schemas.geongan.division import DivisionCreate


def create_division(db: Session, division_in: DivisionCreate):
    db_division = FDivision(**division_in.model_dump())
    db.add(db_division)
    db.commit()
    db.refresh(db_division)
    return db_division


def get_all_division(db: Session):
    return db.query(FDivision).all()
