from unittest.mock import Mock, patch, call, MagicMock, create_autospec
from mock_alchemy.mocking import AlchemyMagicMock, UnifiedAlchemyMagicMock

from src.models.user import User
from src.models.profile import Profile
from src.models.order import Order
from src.models.order_product import OrderProduct
from src.models.order import Order
from src.models.product_category import ProductCategory
from src.models.store_order import StoreOrder
from src.models.category import Category
from src.models.product import Product
from src.mock_test_func.func_for_mock import create_user


def test_mock_create_user():
    '''
    Mock: Подмена сессии и проверка работы создания User.
    Пример функции которую мы замокали:
    def create_user():
        with sync_session() as session:
            user = User(id=5, username='test_user_1', email='test_user@test.com')
            session.add(user)
            session.commit()
    '''
    with patch('src.mock_test_func.func_for_mock.sync_session') as mock_sync_session:
        mock_session = mock_sync_session.return_value.__enter__.return_value
        mock_session.execute.return_value = None

        create_user()

        mock_session.add.assert_called()

        expected_user = User(id=5, username='test_user_1', email='test_user@test.com')
        actual_user = mock_session.add.call_args[0][0]

        assert isinstance(actual_user, User)
        assert actual_user.id == expected_user.id
        assert actual_user.username == expected_user.username
        assert actual_user.email == expected_user.email


def test_mock_wrapper_func():
    '''
    Mock: обращение к БД с подменой сессии и созданием объекта
    '''
    session = UnifiedAlchemyMagicMock()
    session.add(User(id=6, username='test_user_2', email='test_user_2@mail.com'))
    result = session.query(User).first()

    assert isinstance(result, User)
    assert result.id == 6
    assert result.username == 'test_user_2'
