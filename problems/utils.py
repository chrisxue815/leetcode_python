import collections
import json
import os


def json_object_hook(d):
    return collections.namedtuple('Json', d.keys())(*d.values())


def load_json_from_path(path):
    with open(path) as f:
        return json.load(f, object_hook=json_object_hook)


def load_test_json(f):
    f = os.path.splitext(os.path.basename(f))[0]
    f = f.split('_', 1)[0]
    return load_json_from_path('../leetcode_test_cases/{}.json'.format(f))
