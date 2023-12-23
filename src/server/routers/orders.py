import fastapi
from src.server.sql_base.models import Orders
from src.server.resolvers.orders import create, get, delete, update, get_all

router = fastapi.APIRouter(prefix="/Orders", tags=["Orders"])


@router.get("/")
def start_page():
    return ""


@router.post("/create/")
def new_client(orders: Orders):
    return create(orders)


@router.get("/get/{orders_id}")
def search_orders(orders_id: int):
    return get(orders_id)


@router.get("/get/")
def search_all_orders():
    return get_all()


@router.put("/update/{orders_id}")
def upd_orders(orders_id: int, new_data: Orders):
    return update(orders_id, new_data)


@router.delete("/delete/{client_id}")
def del_orders(orders_id: int):
    return delete(orders_id)
