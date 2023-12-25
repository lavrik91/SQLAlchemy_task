from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name_store = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='stores')
    products = relationship('Product', back_populates='store')
    order = relationship('Order', secondary='stores_orders', back_populates='store')
