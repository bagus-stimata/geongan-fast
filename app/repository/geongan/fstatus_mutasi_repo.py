from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.fstatus_mutasi import FStatusMutasi
from app.schemas.geongan.fstatus_mutasi import FStatusMutasiCreate


def create_fstatus_mutasi(db: Session, status_in: FStatusMutasiCreate):
    db_status = FStatusMutasi(**status_in.model_dump(by_alias=True))
    db.add(db_status)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_status)
    return db_status


def get_all_fstatus_mutasi(db: Session):
    return db.query(FStatusMutasi).all()


def get_fstatus_mutasi(db: Session, status_id: int):
    return db.query(FStatusMutasi).filter(FStatusMutasi.id == status_id).first()


def delete_fstatus_mutasi(db: Session, status_id: int):
    db.query(FStatusMutasi).filter(FStatusMutasi.id == status_id).delete()
    db.commit()
