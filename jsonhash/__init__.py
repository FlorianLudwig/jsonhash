import json
import hashlib

def hash(object, algorithm=None):
    """return hash object for object

    object might be None, int, float, dict or array

    """
    if algorithm is None:
        algorithm = hashlib.sha256

    data_string = json.dumps(object,
                             skipkeys=False,
                             ensure_ascii=False,
                             check_circular=True,
                             allow_nan=True,
                             cls=None,
                             indent=None,
                             separators=(',', ':'),
                             encoding="utf-8",
                             default=None,
                             sort_keys=True)

    return algorithm(data_string)
