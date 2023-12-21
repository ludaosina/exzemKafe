from src.server.sql_base.kafe_db import base_worker
from src.server.sql_base.models import Cosmetic


def create(cosmetic: Cosmetic):
    return base_worker.execute(query="INSERT INTO cosmetic(title, cost) VALUES (?, ?) RETURNING id",
                               args=(cosmetic.title, cosmetic.cost))


def get(cosmetic_id: int):
    return base_worker.execute(query="SELECT * FROM cosmetic WHERE id = ?",
                               args=(cosmetic_id,))


def get_all():
    return base_worker.execute(query="SELECT * FROM cosmetic",
                               many=True)


def update(cosmetic_id: int, new_data: Cosmetic):
    return base_worker.execute(query="UPDATE cosmetic SET (title, cost) = (?,?) WHERE id=?",
                               args=(new_data.title, new_data.cost, cosmetic_id))


def delete(cosmetic_id: int):
    return base_worker.execute(query="DELETE FROM cosmetic WHERE id=? ",
                               args=(cosmetic_id,))
