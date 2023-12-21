from pydantic import BaseModel
from typing import List


class ProductInOrder(BaseModel):
    product_id: int
    quantity: int


class CreateOrderSchemas(BaseModel):
    user_id: int
    store_id: int
    order: List[ProductInOrder]
