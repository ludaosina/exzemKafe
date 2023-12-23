from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(pydantic_model=pydantic_models.Staff, database_model=database_models.Staff, prefix='/staff', tags=['Staff']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Post, database_model=database_models.Post, prefix='/posts', tags=['Posts']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.DishCategories, database_model=database_models.DishCategories, prefix='/dish_categories', tags=['DishCategories']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Dishes, database_model=database_models.Dishes, prefix='/dishes', tags=['Dishes']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/users', tags=['Users']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Orders, database_model=database_models.Orders, prefix='/orders', tags=['Orders']).fastapi_router,
    RouterManager(pydantic_model=pydantic_models.Customers, database_model=database_models.Customers, prefix='/customers', tags=['Customers']).fastapi_router
)
