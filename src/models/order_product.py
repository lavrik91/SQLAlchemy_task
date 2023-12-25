from sqlalchemy import Column, ForeignKey, Integer

from src.database import Base


class OrderProduct(Base):
    __tablename__ = 'order_product'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))