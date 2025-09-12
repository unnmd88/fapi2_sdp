from collections.abc import Sequence

import aiofiles
from fastapi import APIRouter
from fastapi import Form, File, UploadFile, Request
from starlette.responses import HTMLResponse

from core.config import UPLOADS_URL
from utils.async_write_files import write_passport_docx

router = APIRouter(tags=['Passport'])
DIR_NAME = UPLOADS_URL / 'passport'


@router.post("/passport-validation")
async def upload_docx(
    err_color: str = Form(...),
    files: Sequence[UploadFile] = File(...),
):
    r = await write_passport_docx(*files)
    return {
        'files': len(files),
        "Filenames": [file.filename for file in files],
    }


@router.get("/", response_class=HTMLResponse)
async def main(request: Request):
    pass