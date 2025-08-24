from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.geogan.fdept import FDept
from app.schemas.geogan.fdept import FDeptCreate


def create_fdept(db: Session, dept_in: FDeptCreate):
    db_dept = FDept(**dept_in.model_dump(by_alias=True))
    db.add(db_dept)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="ID already exists")
    db.refresh(db_dept)
    return db_dept


def get_all_fdept(db: Session):
    return db.query(FDept).all()


def get_fdept(db: Session, dept_id: int):
    return db.query(FDept).filter(FDept.id == dept_id).first()


def delete_fdept(db: Session, dept_id: int):
    db.query(FDept).filter(FDept.id == dept_id).delete()
    db.commit()
