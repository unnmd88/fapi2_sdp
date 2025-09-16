import base64
import io
from collections.abc import Sequence

import aiofiles
import docx
from fastapi import APIRouter
from fastapi import Form, File, UploadFile, Request
from starlette.responses import HTMLResponse, Response
from fastapi.responses import FileResponse

from core.config import UPLOADS_URL
from sdp_lib.passport.api import create_passport
from utils.async_write_files import write_passport_docx


router = APIRouter(tags=['Passport'])
DIR_NAME = UPLOADS_URL / 'passport'


@router.post("/passport-validation")
async def upload_docx(
    err_color: str = Form(...),
    files: Sequence[UploadFile] = File(...),
) :
    passports = []
    for src_file in files:
        doc = docx.Document(src_file.file)
        passp = create_passport(doc)
        passp.get_docx().save('cccaddaaa.docx')
    headers = {'Content-Disposition': 'attachment; filename="zagruzi_a.docx"'}
    return FileResponse(
        'cccaddaaa.docx', headers=headers
    )
    # for src_file in files:
    #     doc = docx.Document(src_file.file)
    #     fs = io.BytesIO()
    #     doc.save(fs)
    #     passports.append(fs)
    #     fs.seek(0)





@router.get("/")
async def main(request: Request):
    return {
        'res': 'hello from sdp-api'
    }