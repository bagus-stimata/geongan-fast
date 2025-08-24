from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geogan.fdatabase import FDatabase
from app.schemas.geogan.fdatabase import FDatabaseCreate


def create_fdatabase(db: Session, database_in: FDatabaseCreate):
    db_database = FDatabase(**database_in.model_dump(by_alias=True))
    db.add(db_database)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_database)
    return db_database


def get_all_fdatabase(db: Session):
    return db.query(FDatabase).all()


def get_fdatabase(db: Session, database_id: int):
    return db.query(FDatabase).filter(FDatabase.id == database_id).first()


def delete_fdatabase(db: Session, database_id: int):
    db.query(FDatabase).filter(FDatabase.id == database_id).delete()
    db.commit()
