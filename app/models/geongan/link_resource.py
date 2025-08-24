from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base


class LinkResource(Base):
    __tablename__ = "link_resources"

    id = Column(Integer, primary_key=True)
    dataset_from_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    dataset_to_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)
