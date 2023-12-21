import json

import pika
from database import sync_session
from models.store import Store
from models.order import Order
from models.order_product import OrderProduct
from models.order import Order
from models.product_category import ProductCategory
from models.store_order import StoreOrder
from models.category import Category
from models.product import Product
from models.profile import Profile
from models.user import User


def create_user():
    with sync_session() as session:
        user = User(id=5, username='test_user_1', email='test_user@test.com')
        session.add(user)
        session.commit()


def send_to_queue(queue_name, message):
    """Фабрика очередей"""
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    connection.close()


def create_order(user, store, orders_data):
    """Создание заказа и отправка информации о нем в очередь"""
    try:
        with sync_session() as session:
            orders = [
                Order(
                    user_id=user,
                    store_id=store,
                    product_id=order_data['product_id'],
                    quantity=order_data['quantity']
                )
                for order_data in orders_data
            ]
            session.add_all(orders)
            session.commit()
            message = 'order created'
    except:
        message = 'The order cannot be placed, please contact technical support.'

    send_to_queue('message', {'user_id': user, 'message': message})


def get_user(user_id):
    with sync_session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        return user


def sending_messages(email, message):
    """Формирование и отправка письма после оформления заказа"""
    return f'Отправка сообщения на {email=}, {message=}'
