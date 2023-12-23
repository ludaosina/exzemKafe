from peewee import Model, CharField, IntegerField, ForeignKeyField
from peewee import *  
import settings


db = SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)

class Post(BaseModel):
    name = CharField(default='')

class Staff(BaseModel):
    user_id = ForeignKeyField(User, backref='staff', default=0)
    post_id = ForeignKeyField(Post, backref='staff', default=0)
    fio = CharField(default='')

class DishCategories(BaseModel):
    name = CharField(default='')

class Customers(BaseModel):
    fio = CharField(default='')
    address = CharField(default='')
    telephone_number = CharField(default='')

class Orders(BaseModel):
    customer_id = ForeignKeyField(Customers, backref='orders', default=0)
    date = CharField(default='')
    total_cost = IntegerField(default=0)

class Dishes(BaseModel):
    category_id = ForeignKeyField(DishCategories, backref='dishes', default=0)
    order_id = ForeignKeyField(Orders, backref='dishes', default=0)
    name = CharField(default='')
    description = CharField(default='')
    price = IntegerField(default=0)

db.create_tables([User, Dishes, Post, DishCategories, Orders, Customers, Staff])