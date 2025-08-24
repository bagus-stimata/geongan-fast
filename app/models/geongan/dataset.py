from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.geongan.link_resource import LinkResource


class Dataset(Base):
    __tablename__ = "datasets"
    __table_args__ = (
        UniqueConstraint("kode1", "division_id", name="uq_datasets_kode1_division"),
    )

    id = Column(Integer, primary_key=True)
    kode1 = Column(String(50), nullable=False)
    description = Column(String(255))
    division_id = Column(Integer, ForeignKey("divisions.id"), nullable=False)
    status_active = Column(Boolean, default=True)
    avatar_image = Column(String(255))
    tr_date = Column(DateTime)
    private = Column(Boolean, default=False)
    relation_key_to_geo = Column(String(255))
    sumber_data = Column(String(255))

    division = relationship("Division", back_populates="datasets")
    files = relationship("DatasetFile", back_populates="dataset", cascade="all, delete-orphan")
    rows = relationship("DatasetRow", back_populates="dataset", cascade="all, delete-orphan")
    links_from = relationship(
        "Dataset",
        secondary="link_resources",
        primaryjoin="Dataset.id == LinkResource.fdatasetFrom",
        secondaryjoin="Dataset.id == LinkResource.fdatasetTo",
        back_populates="links_to",
    )
    links_to = relationship(
        "Dataset",
        secondary="link_resources",
        primaryjoin="Dataset.id == LinkResource.fdatasetTo",
        secondaryjoin="Dataset.id == LinkResource.fdatasetFrom",
        back_populates="links_from",
    )
    endpoint_accesses = relationship("EndpointAccess", back_populates="dataset")
