import fastapi
from src.server.sql_base.models import Customer
from src.server.resolvers.customers import create, get, delete, update, get_all

router = fastapi.APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/")
def start_page():
    return ""


@router.post("/create/")
def new_client(customer: Customer):
    return create(customer)


@router.get("/get/{customer_id}")
def search_client(customer_id: int):
    return get(customer_id)


@router.get("/get/")
def search_all_customers():
    return get_all()


@router.put("/update/{customer_id}")
def upd_client(customer_id: int, new_data: Customer):
    return update(customer_id, new_data)


@router.delete("/delete/{client_id}")
def del_client(customer_id: int):
    return delete(customer_id)
