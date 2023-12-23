from src.server.sql_base.kafe_db import base_worker
from src.server.sql_base.models import Orders


def create(orders: Orders):
    return base_worker.execute(query="INSERT INTO orders(id, customer_id, date, total_cost) VALUES (?, ?, ?, ?) RETURNING id",
                               args=(orders.id, orders.customer_id, orders.date, orders.total_cost))


def get(orders_id: int):
    return base_worker.execute(query="SELECT * FROM orders WHERE id = ?",
                               args=(orders_id,))


def get_all():
    return base_worker.execute(query="SELECT * FROM orders",
                               many=True)


def update(orders_id: int, new_data: Orders):
    return base_worker.execute(query="UPDATE orders SET (id, customer_id, date, total_cost) = (?, ?, ?, ?) WHERE id=?",
                               args=(new_data.id, new_data.customer_id, new_data.date, new_data.total_cost, orders_id))


def delete(orders_id: int):
    return base_worker.execute(query="DELETE FROM orders WHERE id=? ",
                               args=(orders_id,))
