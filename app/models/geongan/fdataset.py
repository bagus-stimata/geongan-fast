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
from app.models.geongan.ft_link_resource import FtLinkResource


class FDataset(Base):
    __tablename__ = "fdataset"
    __table_args__ = (
        UniqueConstraint("kode1", "division_id", name="uq_datasets_kode1_division"),
    )

    id = Column(Integer, primary_key=True)
    kode1 = Column(String(50), nullable=False)
    description = Column(String(255))
    division_id = Column(Integer, ForeignKey("fdivision.id"), nullable=False)
    status_active = Column(Boolean, default=True)
    avatar_image = Column(String(255))
    tr_date = Column(DateTime)
    private = Column(Boolean, default=False)
    relation_key_to_geo = Column(String(255))
    sumber_data = Column(String(255))

    division = relationship("FDivision", back_populates="datasets")
    files = relationship(
        "FDatasetFille", back_populates="fdataset", cascade="all, delete-orphan"
    )
    rows = relationship(
        "FDatasetRow", back_populates="fdataset", cascade="all, delete-orphan"
    )
    links_from = relationship(
        "FDataset",
        secondary="ft_link_resource",
        primaryjoin="FDataset.id == FtLinkResource.fdatasetFrom",
        secondaryjoin="FDataset.id == FtLinkResource.fdatasetTo",
        back_populates="links_to",
    )
    links_to = relationship(
        "FDataset",
        secondary="ft_link_resource",
        primaryjoin="FDataset.id == FtLinkResource.fdatasetTo",
        secondaryjoin="FDataset.id == FtLinkResource.fdatasetFrom",
        back_populates="links_from",
    )
    ft_endpoint_accesses = relationship(
        "FtEndpointAccess", back_populates="fdataset"
    )
