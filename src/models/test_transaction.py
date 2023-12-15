from sqlalchemy import Column, Integer, Float, ForeignKey, String, CheckConstraint
from sqlalchemy.orm import relationship, validates

# from database import Base
#
#
# class BankAccount(Base):
#     __tablename__ = 'bank_accounts'
#
#     account_id = Column(Integer, primary_key=True)
#     balance = Column(Float)
#     title = Column(String)
#
#
# class OrderTest(Base):
#     __tablename__ = 'order_tests'
#
#     id = Column(Integer, primary_key=True)
#     customer_id = Column(Integer, ForeignKey('customers.customer_id'), nullable=False)
#     total_amount = Column(Float, CheckConstraint('total_amount>=0'))
#
#     customer = relationship('Customer', back_populates='order')
#
#     # __table_args__ = (
#     #     CheckConstraint('total_amount >= 0', name='check_total_amount'),
#     # )
#
#     @validates('total_amount')
#     def valid_total_amount(self, key, value):
#         if value < 0:
#             raise ValueError("Total amount must be greater than or equal to 0.")
#         return value
#
#
# class Customer(Base):
#     __tablename__ = 'customers'
#
#     customer_id = Column(Integer, primary_key=True)
#     name = Column(String)
#
#     order = relationship('OrderTest', back_populates='customer')
