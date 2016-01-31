# -*- encoding: utf-8 -*-
import hashlib

import jsonhash

EXAMPLES = [
    None,
    0,
    0.0,
    1,
    'Hello World',
    'Hällö Wáåëþæfg',
    {'Hello': 1, 'hello': 1},
    {'00': 1, '0': 1, '00.0': 1, '000': 1, '00z': 1},
    {},
    [1,2,3,'Hello'],
    {'a': [{'b':1}, None]},
]

def main():
    for example in EXAMPLES:
        h = jsonhash.hash(example)
        print h.hexdigest()


if __name__ == '__main__':
    main()
