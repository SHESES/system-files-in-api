from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
import uvicorn
from modules.test import test_func

router = APIRouter(
    prefix="/api/users",
    tags=["users"],
)


@router.get("/tom")
async def ping():
    return JSONResponse(content={"name": "Tom"}, status_code=200)


@router.get("/alice")
async def err():
    return JSONResponse(content={"name": "Alice"}, status_code=400)


@router.get("/test")
async def run_test_func():
    test_func()
    return {"message": "test_func executed"}


def start_api():
    uvicorn.run(router, host='127.0.0.1', port=6968)


if __name__ == "__main__":
    start_api()
