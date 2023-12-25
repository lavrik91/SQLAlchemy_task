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
        users = [User(**user) for user in users_data]
        stores = [Store(**store) for store in stores]
        products = [Product(**product) for product in products]

        # Добавление всех данных в сессию
        session.add_all(users)
        session.add_all(stores)
        session.add_all(products)
        session.commit()

def send_to_queue(queue_name, message):
    """Фабрика очередей"""
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials, port=5672))
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
