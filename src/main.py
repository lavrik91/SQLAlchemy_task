import asyncio
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from sqlalchemy import exc
from database import sync_session
from models.test_transaction import OrderTest, BankAccount, Customer


# test transaction


def test():
    with sync_session() as session:
        try:
            account1 = BankAccount(balance=1000.00)
            account2 = BankAccount(balance=2000.00)

            session.add_all([account1, account2])
            session.flush()

            account1.balance = 1500.00

            deleted_account2 = session.query(BankAccount).filter_by(account_id=account2.account_id).first()
            session.delete(deleted_account2)

            session.commit()
            print("Transaction successful")
        except Exception as e:
            session.rollback()
            print(f"Transaction failed: {e}")

# test()


def test_2():
    with sync_session() as session:
        try:
            order1 = OrderTest(customer_id=1, total_amount=10)
            session.add(order1)

            # order2 = OrderTest(total_amount=5)
            # session.add(order2)

            order1.total_amount += 50
            # session.flush()
            session.commit()
            print("Transaction successful")
        except exc.IntegrityError as e:
            session.rollback()
            print(f"Transaction failed: {e}")

test_2()