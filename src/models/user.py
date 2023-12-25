from datetime import datetime

from sqlalchemy import text, Column, String, DateTime, Integer
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String)
    create_at = Column(DateTime(), server_default=text("TIMEZONE('utc',now())"))
    update_at = Column(DateTime(), server_default=text("TIMEZONE('utc',now())"),
                       onupdate=datetime.utcnow)
    profile = relationship('Profile', uselist=False, back_populates='user')
    stores = relationship('Store', back_populates='owner')
    orders = relationship('Order', back_populates='user')
