from fastapi import FastAPI
import uvicorn

from routers.users import router as users_router
from routers.messages import router as messages_router

app = FastAPI()

app.include_router(users_router)
app.include_router(messages_router)


def start_api():
    uvicorn.run(app, host='127.0.0.1', port=6968)


if __name__ == "__main__":
    start_api()
