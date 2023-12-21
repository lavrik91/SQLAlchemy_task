from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient
import json

from src.main import app
from src.database import sync_session
from src.models.order import Order


client = TestClient(app)


@pytest.mark.usefixtures('create_test_users')
class TestRabbitMQ:
    """
    Tests: на весь функционал RabbitMQ связанный с созданием заказа
    """

    def test_order_processing(self):
        """Проверка post запроса и правильность передаваемой информации"""
        test_order_data = {
            "user_id": 1,
            "store_id": 1,
            "order": [{"product_id": 1, "quantity": 2}]
        }

        response = client.post("/order", json=test_order_data)
        assert response.status_code == 200
        assert response.request.content == b'{"user_id": 1, "store_id": 1, "order": [{"product_id": 1, "quantity": 2}]}'

    def test_order_bd(self):
        """Проверка заполнения информации в БД"""
        with sync_session() as session:
            order = session.query(Order).filter_by(user_id=1).first()

            assert order.store_id == 1
            assert order.product_id == 1
            assert order.quantity == 2

    def test_process_message(self):
        from src.queues import process_message
        # Мокаем функцию sending_messages, чтобы избежать фактической отправки
        with patch('src.handler.sending_messages') as mock_sending_messages:
            # Здесь создайте тестовые данные, которые будут переданы в функцию
            test_message_data = {
                "user_id": 1,
                "message": "Test message"
            }

            # Конвертируем тестовые данные в формат, который имитирует данные из очереди
            test_message_body = json.dumps(test_message_data).encode('utf-8')

            # Запускаем обработчик с мокнутой функцией sending_messages
            process_message(None, None, None, test_message_body)

            # Проверяем, была ли вызвана мокнутая функция sending_messages
            mock_sending_messages.assert_called_once_with(email='test@example.com', message='Test message')