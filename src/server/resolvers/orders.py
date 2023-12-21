from server.sql_base.pharmacy_db import base_worker
from server.sql_base.models import List


def create_list(list: List):
    return base_worker.execute(query="INSERT INTO list(pharmacy_id, medicines_id) VALUES (?, ?) RETURNING id",
                               args=(list.pharmacy_id, list.medicines_id))


def get_list(list_id: int):
    return base_worker.execute(query="SELECT id, pharmacy_id, medicines_id FROM list WHERE id = ?",
                               args=(list_id,))


def get_all_list():
    return base_worker.execute(query="SELECT id, pharmacy_id, medicines_id FROM list",
                               many=True)


def update_list(list_id: int, new_data: List):
    return base_worker.execute(query="UPDATE list SET pharmacy_id=?, medicines_id=? WHERE id=?",
                               args=(new_data.pharmacy_id, new_data.medicines_id, list_id))


def delete_list(list_id: int):
    return base_worker.execute(query="DELETE FROM list WHERE id=? ",
                               args=(list_id,))
