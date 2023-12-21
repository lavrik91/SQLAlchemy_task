import pika
from fastapi import APIRouter

from .schemas import CreateOrderSchemas

router = APIRouter()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Очередь для обработки заказов
channel.queue_declare(queue='process_orders')


@router.post('/order')
def input_order(input_data: CreateOrderSchemas):
    """Получение информации по заказу"""

    channel.basic_publish(exchange='',
                          routing_key='process_orders',
                          body=input_data.model_dump_json())

    return {"status": "success", "message": "Order successfully submitted"}
