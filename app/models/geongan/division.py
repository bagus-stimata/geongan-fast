from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Division(Base):
    __tablename__ = "divisions"

    id = Column(Integer, primary_key=True)
    kode1 = Column(String(50), nullable=False)
    description = Column(String(255))
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    status_active = Column(Boolean, default=True)

    company = relationship("Company", back_populates="divisions")
    datasets = relationship("Dataset", back_populates="division")
