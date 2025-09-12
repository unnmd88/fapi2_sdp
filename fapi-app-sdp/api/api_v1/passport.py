from collections.abc import Sequence

from fastapi import APIRouter
from fastapi import Form, File, UploadFile, Request
from starlette.responses import HTMLResponse

from core.config import UPLOADS_URL

router = APIRouter(tags=['Passport'])
DIR_NAME = UPLOADS_URL / 'passport'


@router.post("/passport-validation")
def upload_docx(
    err_color: str = Form(...),
    files: Sequence[UploadFile] = File(...),
):
    print(f'color: {err_color}')

    return {
        'files': len(files),
        "Filenames": [file.filename for file in files],
    }


@router.get("/", response_class=HTMLResponse)
async def main(request: Request):
    pass