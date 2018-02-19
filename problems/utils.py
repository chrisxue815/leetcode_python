import collections
import json


def json_object_hook(d):
    return collections.namedtuple('Json', d.keys())(*d.values())


def load_json_from_path(path):
    with open(path) as f:
        return json.load(f, object_hook=json_object_hook)
