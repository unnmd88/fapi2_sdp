import asyncio
from pathlib import Path

import aiofiles
from fastapi import UploadFile

from core.config import UPLOADS_URL, PASSPORTS_DIR
from sdp_lib.utils_common.utils_common import get_curr_datetime


async def write_file(file: UploadFile, filename: str = None):
    async with aiofiles.open(filename or file.filename, 'wb') as f:
        while chunk := await file.read(1024 ** 2):
            await f.write(chunk)
            return filename


async def write_passport_docx(*args: UploadFile):
    async with asyncio.TaskGroup() as tg:
        res = []
        for file in args:
            new_dir = PASSPORTS_DIR / Path(f'{file.filename.rsplit(".", 1)[0]}').name / Path(get_curr_datetime())
            print(f'new_dir: {new_dir}')
            new_dir.mkdir(parents=True, exist_ok=True)
            filename = new_dir / file.filename
            res.append(tg.create_task(write_file(file, filename)) )
    for r in res:
        print(f'r: {r.result()}')
    return res
