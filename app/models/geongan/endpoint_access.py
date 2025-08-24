from enum import IntEnum

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class EndpointType(IntEnum):
    PUBLIC = 0
    PRIVATE = 1
    INTERNAL = 2


class EndpointAccess(Base):
    __tablename__ = "endpoint_accesses"

    id = Column(Integer, primary_key=True)
    userBean = Column(Integer, ForeignKey("users.id"), nullable=False)
    endpoint = Column(String(25), nullable=False)
    fdatasetBean = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    endPointType = Column(Integer, nullable=False)
    basicAuth = Column(String(750))

    user = relationship("User", back_populates="endpoint_accesses")
    dataset = relationship("Dataset", back_populates="endpoint_accesses")

