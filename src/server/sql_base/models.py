from pydantic import BaseModel
from typing import Optional, List


class BaseModelModify(BaseModel):
    id: Optional[int]


class BeautySalon(BaseModel):
    customer_id: int
    fio_customers: str
    quantity: int
    service: str

class Employee(BaseModel):
    id: int
    fio: str
    address: str
    sale_of_cosmetics: bool
    number: str
    experience: int

class Customer(BaseModel):
    id: int
    fio: str
    address: str
    number: str

class SaleOfCosmetics(BaseModel):
    id: int
    client: str
    date_of_purchase: str
    quantity: int
    cost_per_piece: float
    total_cost: float

class Cosmetic(BaseModel):
    id: int
    title: str
    cost: float

class CategoryOfEmployees(BaseModel):
    id: int
    chart: str
    post: str

class Procedure(BaseModel):
    id: int
    title: str
    cost: float

class Services(BaseModel):
    id: int
    cost: float
    date: str
    masters: List[Employee]

class Records(BaseModel):
    id: int
    client_id: int
    employee_id: int
    procedure_id: int
    appointment_date: str
    appointment_time: str

class Review(BaseModel):
    id: int
    client_id: int
    employee_id: int
    rating: int
    comment: str


