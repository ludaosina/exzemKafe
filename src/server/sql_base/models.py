from pydantic import BaseModel
from typing import Optional, List


class BaseModelModify(BaseModel):
    id: Optional[int]


class Users(BaseModel):
    id: int
    login: str
    password: str

class Staff(BaseModel):
    id: int
    users_id: int
    post_id: int
    name: str
    surname: str

class Post(BaseModel):
    id: int
    name: str

class DishCategories(BaseModel):
    id: int
    name: str

class Dishes(BaseModel):
    id: int
    category_id: int
    name: str
    description: str
    price: float

class Orders(BaseModel):
    id: int
    customer_id: int
    date: str
    total_cost: float

class Customer(BaseModel):
    id: int
    name: str
    surname: str
    address: str
    number: str




