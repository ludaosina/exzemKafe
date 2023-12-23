from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: Optional[int] = 0


class ChangePassword(ModifyBaseModel):
    password: str


class LoginData(ModifyBaseModel):
    login: str
    password: str

class User(ModifyBaseModel):
    position: str
    login: str
    password: str
    power_level: int 

class Post(ModifyBaseModel):
    name: str 

class Staff(ModifyBaseModel):
    user_id: int 
    post_id: int 
    fio: str 

class DishCategories(ModifyBaseModel):
    name: str

class Customers(ModifyBaseModel):
    fio: str 
    address: str
    telephone_number: str

class Orders(ModifyBaseModel):
    customer_id: int
    date: str
    total_cost: int

class Dishes(ModifyBaseModel):
    category_id: int 
    order_id: int 
    name: str 
    description: str 
    price: int 