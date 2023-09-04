from fastapi import FastAPI, APIRouter
import json
from fastapi.responses import JSONResponse
import uvicorn

router = APIRouter(
    prefix="/api/messages",
    tags=["messages"],
)


@router.get("/ok")
async def ping():
    return JSONResponse(content={"message": "OK"}, status_code=200)


@router.get("/error")
async def err():
    return JSONResponse(content={"message": "error"}, status_code=400)


def start_api():
    uvicorn.run(router, host='127.0.0.1', port=6968)


if __name__ == "__main__":
    start_api()
