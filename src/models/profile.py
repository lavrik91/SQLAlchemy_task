import enum

from sqlalchemy import Column, String, Date, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship

from database import Base



class StatusUser(enum.Enum):
    buyer = 'buyer'
    seller = 'seller'


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    status = Column(Enum(StatusUser), default=StatusUser.buyer, nullable=False)
    birth_date = Column(Date)
    phone_numder = Column(String(11))
    address = Column(String)
    favorite_product = Column(String)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), unique=True, nullable=False)
    user = relationship('User', back_populates='profile')
