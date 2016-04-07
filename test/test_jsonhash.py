import subprocess
import json

import jsonhash

DATA = [
    {'a': 1},
    {'a': 1, 'b': 2, 'c': 3, 'd': 4},
    [1, 3, 2, 5, 43, 3, 1.25],
    {'a': 'just some dict', '1': [
        'with lists', 1, 'and intergeres',
        {'a': {'and even more': 'stuff', 'c': -1}}
    ]}
]


code = """
import sys
import jsonhash
import json

data = json.load(sys.stdin)
sys.stdout.write(jsonhash.hash(data).hexdigest())
"""


def in_subprocess(data, seed):
    env = {'PYTHONHASHSEED': str(seed)}
    cmd = ['python', '-c', code]
    proc = subprocess.Popen(cmd, env=env, stdin=subprocess.PIPE,
                                          stderr=subprocess.PIPE,
                                          stdout=subprocess.PIPE)
    proc.stdin.write(json.dumps(data))
    proc.stdin.close()
    assert proc.stderr.read() == ''
    return proc.stdout.read()


def compare(data0, data1, algorithm=None):
    assert jsonhash.hash(data0, algorithm).hexdigest() \
           == jsonhash.hash(data1, algorithm).hexdigest()

    # start two subprocesses with different pythonhashseeds to change dict ordering
    assert in_subprocess(data0, 123) == in_subprocess(data1, 321)


def test_jsonjash():
    compare('a', 'a')
    compare(1, 1)
    compare(1.25, 1.25)
    compare(['a'], ['a'])
    compare({1: 'a'}, {1: 'a'})
    compare(DATA, DATA)

    for data in DATA:
        compare(data, data)
