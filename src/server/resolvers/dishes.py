from src.server.sql_base.kafe_db import base_worker
from src.server.sql_base.models import Dishes


def create(dishes: Dishes):
    return base_worker.execute(query="INSERT INTO dishes(category_id, order_id, name, description, price) VALUES (?, ?, ?, ?, ?) RETURNING id",
                               args=(dishes.category_id, dishes.order_id, dishes.name, dishes.description, dishes.price))


def get(dishes_id: int):
    return base_worker.execute(query="SELECT * FROM dishes WHERE id = ?",
                               args=(dishes_id,))


def get_all():
    return base_worker.execute(query="SELECT * FROM dishes",
                               many=True)


def update(dishes_id: int, new_data: Dishes):
    return base_worker.execute(query="UPDATE dishes SET (category_id, order_id, name, description, price) = (?, ?, ?, ?, ?) WHERE id=?",
                               args=(new_data.category_id, new_data.order_id, new_data.name, new_data.description, new_data.price, dishes_id))


def delete(dishes_id: int):
    return base_worker.execute(query="DELETE FROM dishes WHERE id=? ",
                               args=(dishes_id,))
