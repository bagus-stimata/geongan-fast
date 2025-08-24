from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class DatasetFile(Base):
    __tablename__ = "dataset_files"

    id = Column(Integer, primary_key=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False, index=True)
    file_name = Column(String(255), nullable=False)
    file_type = Column(String(100))
    jenis = Column(String(50))
    flag = Column(String(50))
    description = Column(String(255))
    kode1 = Column(String(50))

    dataset = relationship("Dataset", back_populates="files")
