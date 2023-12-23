import fastapi
from src.server.sql_base.models import Dishes
from src.server.resolvers.dishes import create, get, delete, update, get_all

router = fastapi.APIRouter(prefix="/dishes", tags=["Dishes"])


@router.get("/")
def start_page():
    return ""


@router.post("/create/")
def new_dishes(dishes: Dishes):
    return create(dishes)


@router.get("/get/{dishes_id}")
def search_dishes(dishes_id: int):
    return get(dishes_id)


@router.get("/get/")
def search_all_dishes():
    return get_all()


@router.put("/update/{dishes_id}")
def upd_dishes(dishes: int, new_data: Dishes):
    return update(dishes_id, new_data)


@router.delete("/delete/{dishes_id}")
def del_dishes(dishes_id: int):
    return delete(dishes_id)
