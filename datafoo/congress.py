import json
from os.path import join
CACHE_DIR = join('datafoo', 'cache')


def get_legislators():
    fname = join(CACHE_DIR, 'legislators-current.json')
    with open(fname, 'r') as rf:
        data = json.load(rf)
    return data
