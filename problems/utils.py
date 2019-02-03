import collections
import json
import os


def json_object_hook(d):
    return collections.namedtuple('Json', list(d.keys()))(*list(d.values()))


def load_json_from_path(path):
    with open(path) as f:
        return json.load(f, object_hook=json_object_hook)


def load_test_json(f):
    f = os.path.splitext(os.path.basename(f))[0]
    prefix, id = f.split('_', 2)[:2]
    return load_json_from_path('../leetcode_test_cases/{}_{}.json'.format(prefix, id))
