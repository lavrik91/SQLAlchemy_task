import enum
from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, text
from sqlalchemy.orm import relationship

from database import Base


class StatusOrder(enum.Enum):
    processing = 'processing'
    sent = 'sent'
    delivered = 'delivered'


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    status_order = Column(Enum(StatusOrder), default=StatusOrder.processing, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    create_at = Column(DateTime(), server_default=text("TIMEZONE('utc',now())"))
    update_at = Column(DateTime(), server_default=text("TIMEZONE('utc',now())"),
                       onupdate=datetime.utcnow)
    user = relationship('User', back_populates='orders')
    products = relationship('Product', secondary='product_category', back_populates='orders')
    store = relationship('Store', secondary='stores_orders', back_populates='stores')
