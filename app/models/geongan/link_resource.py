from sqlalchemy import Column, Integer, ForeignKey

from app.core.database import Base


class LinkResource(Base):
    __tablename__ = "link_resources"

    id = Column(Integer, primary_key=True)
    fdatasetFrom = Column(Integer, ForeignKey("datasets.id"), nullable=False)
    fdatasetTo = Column(Integer, ForeignKey("datasets.id"), nullable=False)

