from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class EndpointAccess(Base):
    __tablename__ = "endpoint_accesses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    endpoint = Column(String(255), nullable=False)
    dataset_id = Column(Integer, ForeignKey("datasets.id"))
    endpoint_type = Column(String(50))
    basic_auth = Column(String(255))

    user = relationship("User", back_populates="endpoint_accesses")
    dataset = relationship("Dataset", back_populates="endpoint_accesses")
