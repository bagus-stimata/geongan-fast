from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    Date,
    Index,
)
from sqlalchemy.orm import relationship
from app.core.database import Base


class DatasetRow(Base):
    __tablename__ = "dataset_rows"
    __table_args__ = (Index("ix_dataset_rows_dataset_id", "dataset_id"),)

    id = Column(Integer, primary_key=True)
    kode1 = Column(String(50))
    description = Column(String(255))
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    fsatuan_id = Column(Integer)
    evalue_type = Column(String(50))
    str_value1 = Column(String(255))
    int_value1 = Column(Integer)
    double_value1 = Column(Float)
    date_value1 = Column(Date)

    dataset = relationship("Dataset", back_populates="rows")
