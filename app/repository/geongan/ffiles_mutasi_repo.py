from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.ffiles_mutasi import FFilesMutasi
from app.schemas.geongan.ffiles_mutasi import FFilesMutasiCreate


def create_ffiles_mutasi(db: Session, file_in: FFilesMutasiCreate):
    db_file = FFilesMutasi(**file_in.model_dump(by_alias=True))
    db.add(db_file)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_file)
    return db_file


def get_all_ffiles_mutasi(db: Session):
    return db.query(FFilesMutasi).all()


def get_ffiles_mutasi(db: Session, file_id: int):
    return db.query(FFilesMutasi).filter(FFilesMutasi.id == file_id).first()


def delete_ffiles_mutasi(db: Session, file_id: int):
    db.query(FFilesMutasi).filter(FFilesMutasi.id == file_id).delete()
    db.commit()
