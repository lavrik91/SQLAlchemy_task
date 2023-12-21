import pika
import json
from mock_test_func.func_for_mock import create_order, sending_messages, get_user


def process_order(ch, method, properties, body):
    """Обработка заказа и добавление его в БД"""

    order = json.loads(body.decode('utf-8'))
    user = order['user_id']
    store = order['store_id']
    orders_data = order['order']
    create_order(user, store, orders_data)


def process_message(ch, method, properties, body):
    """
    Получение информации об успешном/неуспешном создании заказа
    и отправка сообщения на почту покупателя.
    sending_messages: отправка сообщения покупателю
    """
    body = json.loads(body.decode('utf-8'))
    user = get_user(body['user_id'])
    post = sending_messages(email=user.email, message=body['message'])
    print(f'{post=}')


def main():
    """Обработка очередей"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Создание очереди для заказов
    channel.queue_declare(queue='process_orders')
    channel.queue_declare(queue='message')

    channel.basic_qos(prefetch_count=1)

    # Установка обработчика для очереди
    channel.basic_consume(queue='process_orders', on_message_callback=process_order, auto_ack=True)
    channel.basic_consume(queue='message', on_message_callback=process_message, auto_ack=True)

    print('Order processor is waiting for orders. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
