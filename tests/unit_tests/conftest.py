import pytest
from sqlalchemy import delete

from src.database import sync_session
from src.models.profile import Profile
from src.models.order_product import OrderProduct
from src.models.order import Order
from src.models.product_category import ProductCategory
from src.models.store_order import StoreOrder
from src.models.category import Category
from src.models.user import User
from src.models.store import Store
from src.models.product import Product


@pytest.fixture(scope='session')
def create_test_users():
    users_data = [
        {"id": 1, "username": "user1", "email": "user1@example.com"},
        {"id": 2, "username": "user2", "email": "user2@example.com"},
        {"id": 3, "username": "user3", "email": "user3@example.com"},
    ]

    stores = [
        {'id': 1, 'name_store': 'name_store_1', 'owner_id': 1},
        {'id': 2, 'name_store': 'name_store_2', 'owner_id': 2},
    ]

    products = [
        {'id': 1, 'title': 'apple', 'price': 100.00, 'quantity': 1000, 'store_id': 1},
        {'id': 2, 'title': 'orange', 'price': 85.50, 'quantity': 1400, 'store_id': 1},
        {'id': 3, 'title': 'iphone', 'price': 100000.50, 'quantity': 22, 'store_id': 2},
    ]

    with sync_session() as session:
        # Удаление всех данных в порядке, обратном их зависимости
        stmt_order = delete(Order)
        stmt_product = delete(Product)
        stmt_store = delete(Store)
        stmt_profile = delete(Profile)
        stmt_user = delete(User)

        session.execute(stmt_order)
        session.execute(stmt_product)
        session.execute(stmt_store)
        session.execute(stmt_user)
        session.execute(stmt_profile)

        users = [User(**user) for user in users_data]
        stores = [Store(**store) for store in stores]
        products = [Product(**product) for product in products]

        # Добавление всех данных в сессию
        session.add_all(users)
        session.add_all(stores)
        session.add_all(products)
        session.commit()

        # return session.query(Store)
