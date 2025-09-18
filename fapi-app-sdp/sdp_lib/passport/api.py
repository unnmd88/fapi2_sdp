from docx import Document

from sdp_lib.passport.passport import Passport
from sdp_lib.passport.validation.common_validators import check_is_directions_table
from sdp_lib.passport.validation.dt_validators import validate_and_create_directions_table
from sdp_lib.utils_common.utils_common import to_json


def create_passport(
    filename: str,
    docx: Document,
) -> Passport:
    """
    Проверяет ошибки и создает паспорт светофорного объекта.
    :param filename: Имя(путь) файла.
    :param docx: Исходный docx файл.
    :return: Экземпляр паспорта.
    """
    passport = Passport(filename, docx)
    for i, table in enumerate(docx.tables):
        if check_is_directions_table(table.rows):
            print('Direction table was found')
            passport.load_direction_table(validate_and_create_directions_table(i, table))
    return passport


if __name__ == '__main__':
    path5 = '/home/auser/py.projects/sdp_lib/sdp_lib/passport/СО_2094_ул_Островитянова_ул_Ак_Волгина_2.docx'
    path6 = '/home/auser/py.projects/sdp_lib/sdp_lib/passport/passport2/validation/ПД Паспорт шаблон 2025.docx'
    path7 = '/home/auser/py.projects/sdp_lib/sdp_lib/passport/СО_72_Тургеневская_пл_Мясницкая_ул_Сретенский_б_р_Чистопрудный_б.docx'
    the_passport = create_passport('result.docx', Document(path7))
    print(f'the_passport: {the_passport}')
