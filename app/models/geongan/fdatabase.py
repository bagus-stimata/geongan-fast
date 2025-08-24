from sqlalchemy import Column, Integer, String, Boolean, DateTime, text
from datetime import datetime

from app.core.database import Base


class FDatabase(Base):
    __tablename__ = "fdatabase"

    id = Column(Integer, primary_key=True, index=True)
    kode1 = Column(String(20), default="", nullable=False)
    kode2 = Column(String(20), default="", nullable=False)
    description = Column(String(100), default="", nullable=False)
    version = Column(Integer, default=0, nullable=True)
    uuid = Column(String(50), default="", nullable=True)
    vendorDb = Column(String(100), default="", nullable=True)
    serverOs = Column(String(100), default="", nullable=True)
    statusActive = Column(Boolean, nullable=False, server_default=text("true"))
    fcompanyBean = Column(Integer, default=0, nullable=False)
    dbVersion = Column(String(20), default="", nullable=True)
    serverData = Column(String(100), default="", nullable=True)
    created = Column(DateTime, default=datetime.utcnow)
    modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modifiedBy = Column(String(30), default="", nullable=True)
