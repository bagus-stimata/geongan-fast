from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geogan.fproses_mutasi import FProsesMutasi
from app.schemas.geogan.fproses_mutasi import FProsesMutasiCreate


def create_fproses_mutasi(db: Session, proses_in: FProsesMutasiCreate):
    db_proses = FProsesMutasi(**proses_in.model_dump(by_alias=True))
    db.add(db_proses)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_proses)
    return db_proses


def get_all_fproses_mutasi(db: Session):
    return db.query(FProsesMutasi).all()


def get_fproses_mutasi(db: Session, proses_id: int):
    return db.query(FProsesMutasi).filter(FProsesMutasi.id == proses_id).first()


def delete_fproses_mutasi(db: Session, proses_id: int):
    db.query(FProsesMutasi).filter(FProsesMutasi.id == proses_id).delete()
    db.commit()
