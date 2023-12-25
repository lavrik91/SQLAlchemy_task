import pika
from fastapi import APIRouter

from mock_test_func.func_for_mock import create_user
from .schemas import CreateOrderSchemas

router = APIRouter()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials, port=5672))
channel = connection.channel()

# Очередь для обработки заказов
channel.queue_declare(queue='process_orders')

@router.get('/create_bd')
def create_bd():
    create_user()


@router.post('/order')
def input_order(input_data: CreateOrderSchemas):
    """Получение информации по заказу"""

    channel.basic_publish(exchange='',
                          routing_key='process_orders',
                          body=input_data.model_dump_json())

    return {"status": "success", "message": "Order successfully submitted"}
