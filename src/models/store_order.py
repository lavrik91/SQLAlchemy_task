from sqlalchemy import Column, ForeignKey, Integer

from src.database import Base


class StoreOrder(Base):
    __tablename__ = 'stores_orders'

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('stores.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
