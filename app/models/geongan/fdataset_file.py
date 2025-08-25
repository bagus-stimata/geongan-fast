from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class FDatasetFille(Base):
    __tablename__ = "fdataset_fille"

    id = Column(Integer, primary_key=True)
    fdataset_id = Column(Integer, ForeignKey("fdataset.id"), nullable=False, index=True)
    file_name = Column(String(255), nullable=False)
    file_type = Column(String(100))
    jenis = Column(String(50))
    flag = Column(String(50))
    description = Column(String(255))
    kode1 = Column(String(50))

    fdataset = relationship("FDataset", back_populates="files")
