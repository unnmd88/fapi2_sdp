import os
from os import mkdir
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = BASE_DIR / 'media'
UPLOADS_URL = BASE_DIR / 'media/uploads'


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8181


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    passport: str = '/passport'


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()


uploads_dir = Path(UPLOADS_URL)
uploads_dir.mkdir(parents=True, exist_ok=True)

