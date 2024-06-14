from fastapi import APIRouter, FastAPI
import uvicorn
from src.backend.app.employee.endpoints import employee_router

app = FastAPI()
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@app.get("/test/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

app.include_router(router)
app.include_router(employee_router)

