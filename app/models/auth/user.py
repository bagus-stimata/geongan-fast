from sqlalchemy import Column, Integer, String, Date, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("username", "email", name="uq_users_username_email"),)

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    roles = relationship("Role", secondary="users_roles", back_populates="users")
    fdivisionBean = Column(Integer, nullable=True)
    organizationLevel = Column(String(50), nullable=True)
    phone = Column(Integer, nullable=True)
    countryCode = Column(Integer, nullable=True)
    avatarImage = Column(String(255), nullable=True)
    birthDate = Column(Date, nullable=True)
    endpoint_accesses = relationship(
        "FtEndpointAccess", back_populates="user", cascade="all, delete-orphan"
    )

