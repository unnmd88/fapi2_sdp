from collections.abc import Iterable, Sequence
from pathlib import Path
from zipfile import ZipFile

import aiofiles
from fastapi import UploadFile

from core.config import PASSPORTS_DIR
from sdp_lib.passport.passport import Passport
from sdp_lib.utils_common.utils_common import get_curr_datetime


doc_suffixes = {'.docx', '.doc'}

def get_filepath_with_docx_suffix(parent_dir: str, filename: str) -> Path:
    filename = Path(filename)
    return  Path(parent_dir) / filename if filename.suffix in doc_suffixes else f'{filename}.docx'


def mkdir_for_new_passport_file():
    parent_dir = PASSPORTS_DIR / get_curr_datetime()
    parent_dir.mkdir(parents=True, exist_ok=True)
    return parent_dir


def save_and_zip_passport_docx(
    passports: Iterable[Passport],
):
    """
    Сохраняет документ как word файл у каждого объекта passports и добавляет в архив.
    :param passports: Итератор с объектами Passport.
    :return: Путь к zip архиву.
    """
    parent_dir = mkdir_for_new_passport_file()
    with ZipFile(f'{parent_dir}/results.zip', 'a') as obj_zip:
        for passport in passports:
            p = passport.filename
            filepath = get_filepath_with_docx_suffix(parent_dir, p)
            passport.get_docx().save(filepath)
            obj_zip.write(filepath, arcname=p)
        return obj_zip.filename


class PassportSaver:
    """ Сохраняет паспорта на диск, формирует zip-архив.  """

    def __init__(self, passports: Sequence[Passport]):
        self.passports = passports
        if not passports:
            raise ValueError(f'passports cant be empty.')
        self.parent_dir = mkdir_for_new_passport_file()

    def save_and_get_as_docx_if_only_one_else_as_zip_archive(self) -> Path:
        """
        Сохраняет паспорта в word формате из экземпляров Passport(self.passport).
        Если в последовательности self.passport один экземпляр - вернёт ссылку на word,
        если более одного - упакует все word в архив zip и вернёт на него ссылку(экземпляр Path).
        :return: Экземпляр Path документа word или архива zip.
        """
        if len(self.passports) == 1:
            passport = self.passports[0]
            filepath = get_filepath_with_docx_suffix(self.parent_dir, passport.filename)
            passport.get_docx().save(filepath)
            return filepath
        return self.save_and_get_as_zip()

    def save_and_get_as_zip(self):
        """
        Сохраняет документ как word файл у каждого объекта passports и добавляет в архив.
        :return: Путь к zip архиву.
        """
        with ZipFile(f'{self.parent_dir}/results.zip', 'a') as obj_zip:
            for passport in self.passports:
                p = passport.filename
                filepath = get_filepath_with_docx_suffix(self.parent_dir, p)
                passport.get_docx().save(filepath)
                obj_zip.write(filepath, arcname=p)
                filepath.unlink()
            return Path(obj_zip.filename)