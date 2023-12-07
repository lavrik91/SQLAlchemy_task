from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Numeric)
    quantity = Column(Integer)
    store_id = Column(Integer, ForeignKey('stores.id'))
    store = relationship('Store', back_populates='products')
    categories = relationship('Category', secondary='product_category', back_populates='product')
