from src.server.sql_base.kafe_db import base_worker
from src.server.sql_base.models import Customer


def create(customer: Customer):
    return base_worker.execute(query="INSERT INTO customers(id, FIO, address, number) VALUES (?, ?, ?, ?) RETURNING id",
                               args=(customer.id, customer.fio, customer.address, customer.number))


def get(customer_id: int):
    return base_worker.execute(query="SELECT * FROM customers WHERE id = ?",
                               args=(customer_id,))


def get_all():
    return base_worker.execute(query="SELECT * FROM customers",
                               many=True)


def update(customer_id: int, new_data: Customer):
    return base_worker.execute(query="UPDATE customers SET (id,FIO,address,number) = (?,?,?,?) WHERE id=?",
                               args=(new_data.id, new_data.fio, new_data.address, new_data.number, customer_id))


def delete(customer_id: int):
    return base_worker.execute(query="DELETE FROM customers WHERE id=? ",
                               args=(customer_id,))
