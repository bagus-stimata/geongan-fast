from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base


class FCompany(Base):
    __tablename__ = "fcompany"

    id = Column(Integer, primary_key=True)
    kode1 = Column(String(50), nullable=False)
    description = Column(String(255))
    status_active = Column(Boolean, default=True)

    divisions = relationship("FDivision", back_populates="company")
