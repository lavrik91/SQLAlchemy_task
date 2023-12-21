import pytest
from decimal import Decimal
from src.database import sync_session
from src.models.user import User
from src.models.store import Store
from src.models.product import Product


@pytest.mark.usefixtures('create_test_users')
class TestModelDB:
    def test_count_users(self):
        with sync_session() as session:
            users = session.query(User)

        assert users.count() == 3

    def test_name_store(self):
        with sync_session() as session:
            store = session.query(Store).filter_by(id=1).first()

        assert store.name_store == 'name_store_1'

    @pytest.mark.parametrize(
        'id_product, price_product',
        [
            (1, Decimal(100.00)),
            (2, Decimal(85.50)),
            pytest.param(3, Decimal(0), marks=pytest.mark.xfail),
        ]
    )
    def test_product(self, id_product, price_product):
        with sync_session() as session:
            product = session.query(Product).filter_by(id=id_product).first()

        assert product.price == price_product
