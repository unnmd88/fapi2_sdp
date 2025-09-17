import uvicorn
from fastapi import FastAPI
from api import router as api_router

from core.config import settings


app = FastAPI()
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.run_deb_vbox.host,
        port=settings.run_deb_vbox.port,
        reload=True,
    )
