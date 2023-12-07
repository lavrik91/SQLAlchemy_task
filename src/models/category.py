from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name_category = Column(String)
    product = relationship('Product', secondary='product_category', back_populates='categories')
