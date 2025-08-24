from sqlalchemy import Column, Integer, ForeignKey

from app.core.database import Base


class FtLinkResource(Base):
    __tablename__ = "ft_link_resource"

    id = Column(Integer, primary_key=True)
    fdatasetFrom = Column(Integer, ForeignKey("fdataset.id"), nullable=False)
    fdatasetTo = Column(Integer, ForeignKey("fdataset.id"), nullable=False)

