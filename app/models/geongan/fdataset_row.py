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


class FDatasetRow(Base):
    __tablename__ = "fdataset_row"
    __table_args__ = (Index("ix_fdataset_row_fdataset_id", "fdataset_id"),)

    id = Column(Integer, primary_key=True)
    kode1 = Column(String(50))
    description = Column(String(255))
    fdataset_id = Column(Integer, ForeignKey("fdataset.id"), nullable=False)
    fsatuan_id = Column(Integer)
    evalue_type = Column(String(50))
    str_value1 = Column(String(255))
    int_value1 = Column(Integer)
    double_value1 = Column(Float)
    date_value1 = Column(Date)

    fdataset = relationship("FDataset", back_populates="rows")
