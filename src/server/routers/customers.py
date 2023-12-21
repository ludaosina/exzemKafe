import fastapi
from server.sql_base.models import Client
from server.resolvers.client import create_client, get_client, delete_client, update_client, get_all_client

client_router = fastapi.APIRouter(prefix="/client", tags=["Client"])


@client_router.get("/")
def start_page():
    return ""


@client_router.post("/create/")
def new_client(client: Client):
    return create_client(client)


@client_router.get("/get/{client_id}")
def search_client(client_id: int):
    return get_client(client_id)


@client_router.get("/get/")
def search_all_clients():
    return get_all_client()


@client_router.put("/update/{client_id}")
def upd_client(client_id: int, new_data: Client):
    return update_client(client_id, new_data)


@client_router.delete("/delete/{client_id}")
def del_client(client_id: int):
    return delete_client(client_id)
