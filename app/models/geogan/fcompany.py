from sqlalchemy import Column, Integer, String, Boolean, DateTime, text
from datetime import datetime

from app.core.database import Base


class FCompany(Base):
    __tablename__ = "fcompany"

    id = Column(Integer, primary_key=True, index=True)
    kode1 = Column(String(20), default="", nullable=False)
    kode2 = Column(String(20), default="", nullable=False)
    description = Column(String(100), default="", nullable=False)
    alamat1 = Column(String(400), default="", nullable=True)
    alamat2 = Column(String(400), default="", nullable=True)
    telp = Column(String(20), default="", nullable=True)
    email = Column(String(50), default="", nullable=True)
    website = Column(String(50), default="", nullable=True)
    statusActive = Column(Boolean, nullable=False, server_default=text("true"))
    created = Column(DateTime, default=datetime.utcnow)
    modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modifiedBy = Column(String(30), default="", nullable=True)
