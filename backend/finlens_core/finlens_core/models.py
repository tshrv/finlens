import uuid

from sqlalchemy import Column, Date, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from src.database import Base as _Base


class Base(_Base):
    __abstract__ = True
    _registry = set()

    def __init_subclass__(cls):
        Base._registry.add(cls)

    def __repr__(self):
        dc = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        attrs = ", ".join([f"{k}={v}" for k, v in dc.items()])
        return f"<{self.__class__.__name__}({attrs})>"


class Bank(Base):
    __tablename__ = "banks"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    code = Column(String(12), unique=True, index=True, nullable=False)

    bank_accounts = relationship("BankAccount", back_populates="bank")


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    pan = Column(String(10), unique=True, index=True, nullable=False)
    name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    address = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    bank_accounts = relationship("BankAccount", back_populates="user")


class BankAccount(Base):
    __tablename__ = "bank_accounts"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    number = Column(String(22), unique=True, index=True, nullable=False)
    date_of_opening = Column(Date, nullable=False)
    bank_id = Column(String(36), ForeignKey("banks.id"), nullable=False)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)

    bank = relationship("Bank", back_populates="bank_accounts")
    user = relationship("User", back_populates="bank_accounts")
