from src.server.sql_base.kafe_db import base_worker
from src.server.sql_base.models import Users


def create(users: Users):
    return base_worker.execute(query="INSERT INTO users(id, login, password) VALUES (?, ?, ?) RETURNING id",
                               args=(users.id, users.login, users.password))


def get(users_id: int):
    return base_worker.execute(query="SELECT * FROM users WHERE id = ?",
                               args=(users_id,))


def get_all():
    return base_worker.execute(query="SELECT * FROM users",
                               many=True)


def update(users_id: int, new_data: Users):
    return base_worker.execute(query="UPDATE users SET (id, login, password) = (?,?,?) WHERE id=?",
                               args=(new_data.id, new_data.login, new_data.password, users_id))


def delete(users_id: int):
    return base_worker.execute(query="DELETE FROM users WHERE id=? ",
                               args=(users_id,))
