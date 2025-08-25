from sqlalchemy.orm import Session

from app.models.geongan.fdivision import FDivision
from app.schemas.geongan.fdivision import FDivisionCreate


def create_fdivision(db: Session, fdivision_in: FDivisionCreate):
    db_fdivision = FDivision(**fdivision_in.model_dump())
    db.add(db_fdivision)
    db.commit()
    db.refresh(db_fdivision)
    return db_fdivision


def get_all_fdivision(db: Session):
    return db.query(FDivision).all()
