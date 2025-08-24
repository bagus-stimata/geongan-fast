from enum import IntEnum

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class EndpointType(IntEnum):
    PUBLIC = 0
    PRIVATE = 1
    INTERNAL = 2


class FtEndpointAccess(Base):
    __tablename__ = "ft_endpoint_access"

    id = Column(Integer, primary_key=True)
    userBean = Column(Integer, ForeignKey("users.id"), nullable=False)
    endpoint = Column(String(25), nullable=False)
    fdatasetBean = Column(Integer, ForeignKey("fdataset.id"), nullable=False)
    endPointType = Column(Integer, nullable=False)
    basicAuth = Column(String(750))

    user = relationship("User", back_populates="endpoint_accesses")
    dataset = relationship("FDataset", back_populates="endpoint_accesses")

