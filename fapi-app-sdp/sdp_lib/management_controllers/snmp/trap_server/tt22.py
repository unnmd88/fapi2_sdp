import pprint
import sys
import tomllib
from collections.abc import MutableMapping
from pathlib import Path


p = Path('err_log.log')
print(f'path: {p}')
print(f'path: {p.absolute()}')
print(f'path: {p.owner()}')


