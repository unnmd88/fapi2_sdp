import uvicorn
from fastapi import FastAPI
from api import router as api_router

from core.config import settings


app = FastAPI()
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.run_localhost.host,
        port=settings.run_localhost.port,
        reload=True,
    )
