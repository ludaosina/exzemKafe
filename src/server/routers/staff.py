import fastapi
from src.server.sql_base.models import Staff
from src.server.resolvers.staff import create, get, delete, update, get_all

router = fastapi.APIRouter(prefix="/staff", tags=["Staff"])


@router.get("/")
def start_page():
    return ""


@router.post("/create/")
def new_client(staff: Staff):
    return create(staff)


@router.get("/get/{staff_id}")
def search_staff(staff_id: int):
    return get(staff_id)


@router.get("/get/")
def search_all_staff():
    return get_all()


@router.put("/update/{staff_id}")
def upd_staff(staff_id: int, new_data: Staff):
    return update(staff_id, new_data)


@router.delete("/delete/{client_id}")
def del_staff(staff_id: int):
    return delete(staff_id)
