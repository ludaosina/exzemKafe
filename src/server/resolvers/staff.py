from src.server.sql_base.kafe_db import base_worker
from src.server.sql_base.models import Staff


def create(staff: Staff):
    return base_worker.execute(query="INSERT INTO staff(id, users_id, post_id, name, surname) VALUES (?, ?, ?, ?, ?) RETURNING id",
                               args=(staff.id, staff.name, staff.surname, staff.address, staff.number))


def get(staff_id: int):
    return base_worker.execute(query="SELECT * FROM staff WHERE id = ?",
                               args=(staff_id,))


def get_all():
    return base_worker.execute(query="SELECT * FROM staff",
                               many=True)


def update(staff_id: int, new_data: Staff):
    return base_worker.execute(query="UPDATE staff SET (id, users_id, post_id, name, surname) = (?, ?, ?, ?, ?) WHERE id=?",
                               args=(new_data.id, new_data.name, new_data.surname, new_data.address, new_data.number, staff_id))


def delete(staff_id: int):
    return base_worker.execute(query="DELETE FROM staff WHERE id=? ",
                               args=(staff_id,))
