from fastapi import APIRouter

from core.config import settings
from .passport import router as passport_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    passport_router,
    prefix=settings.api.v1.passport,
)
