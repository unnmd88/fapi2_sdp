import asyncio
from pathlib import Path

import aiofiles
from fastapi import UploadFile

from core.config import UPLOADS_URL, PASSPORTS_DIR


async def asave_uploaded_file(filepath):
    async with aiofiles.open(filepath, 'wb') as f:
        while chunk := await filepath.read(1024 ** 2):
            await f.write(chunk)
        return filepath


async def write_passport_docx(*args: UploadFile):
    async with asyncio.TaskGroup() as tg:
        res = []
        for file in args:
            new_dir = PASSPORTS_DIR / Path(f'{file.filename.rsplit(".", 1)[0]}').name
            print(f'new_dir: {new_dir}')
            new_dir.mkdir(parents=True, exist_ok=True)
            filename = new_dir / file.filename
            res.append(tg.create_task(save_uploaded_file(file, filename)))
    for r in res:
        print(f'r: {r.result()}')
    return res
