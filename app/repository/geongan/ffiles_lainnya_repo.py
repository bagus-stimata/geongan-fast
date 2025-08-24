from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geongan.ffiles_lainnya import FFilesLainnya
from app.schemas.geongan.ffiles_lainnya import FFilesLainnyaCreate


def create_ffiles_lainnya(db: Session, file_in: FFilesLainnyaCreate):
    db_file = FFilesLainnya(**file_in.model_dump(by_alias=True))
    db.add(db_file)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_file)
    return db_file


def get_all_ffiles_lainnya(db: Session):
    return db.query(FFilesLainnya).all()


def get_ffiles_lainnya(db: Session, file_id: int):
    return db.query(FFilesLainnya).filter(FFilesLainnya.id == file_id).first()


def delete_ffiles_lainnya(db: Session, file_id: int):
    db.query(FFilesLainnya).filter(FFilesLainnya.id == file_id).delete()
    db.commit()
