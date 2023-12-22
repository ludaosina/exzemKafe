import fastapi
from src.server.sql_base.models import Client
from src.server.resolvers.customers import create, get, delete, update, get_all

router = fastapi.APIRouter(prefix="/client", tags=["Client"])


@router.get("/")
def start_page():
    return ""


@router.post("/create/")
def new_client(client: Client):
    return create(client)


@router.get("/get/{client_id}")
def search_client(client_id: int):
    return get(client_id)


@router.get("/get/")
def search_all_clients():
    return get_all()


@router.put("/update/{client_id}")
def upd_client(client_id: int, new_data: Client):
    return update(client_id, new_data)


@router.delete("/delete/{client_id}")
def del_client(client_id: int):
    return delete(client_id)
