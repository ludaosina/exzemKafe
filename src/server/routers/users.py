import fastapi
from src.server.sql_base.models import User
from src.server.resolvers.users import create, get, delete, update, get_all

router = fastapi.APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def start_page():
    return ""


@router.post("/create/")
def new_users(users: User):
    return create(users)


@router.get("/get/{users_id}")
def search_users(users_id: int):
    return get(users_id)


@router.get("/get/")
def search_all_users():
    return get_all()


@router.put("/update/{users_id}")
def upd_client(users_id: int, new_data: Users):
    return update(users_id, new_data)


@router.delete("/delete/{users_id}")
def del_users(users_id: int):
    return delete(users_id)
