from sqlalchemy import Column, Integer, String, Boolean, DateTime, text
from datetime import datetime

from app.core.database import Base


class FFilesMutasi(Base):
    __tablename__ = "ffilesmutasi"

    id = Column(Integer, primary_key=True, index=True)
    kode1 = Column(String(20), default="", nullable=False)
    kode2 = Column(String(20), default="", nullable=False)
    description = Column(String(100), default="", nullable=False)
    fileName = Column(String(100), default="", nullable=True)
    fileSize = Column(Integer, default=0, nullable=True)
    statusActive = Column(Boolean, nullable=False, server_default=text("true"))
    created = Column(DateTime, default=datetime.utcnow)
    modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modifiedBy = Column(String(30), default="", nullable=True)
