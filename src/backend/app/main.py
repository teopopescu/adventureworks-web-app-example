from fastapi import APIRouter, FastAPI, Request, Response
import uvicorn
from src.backend.app.employee.endpoints import employee_router
import time
app = FastAPI()

router = APIRouter()


@router.get("/")
async def hello_world():
    return {"Hello":"World"}

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@app.get("/test/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

app.include_router(router)
app.include_router(employee_router)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    now = time.time()
    one_hour_later = now + 3600
    response.set_cookie(key="last_request_date", value=now)
    response.set_cookie(key="expiration_time", value=one_hour_later)
    return response
