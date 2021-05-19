import json
import os
import types

from linkedlist import ListNode
from tree import TreeNode


def test(tst, file, solution, func=None, process_case=None, process_args=None, process_result=None, check_result=None):
    if not func:
        func_name = next(f for f in dir(solution) if not f.startswith('__'))
        func = getattr(solution, func_name)

    cases = load_test_json(file).test_cases

    for case in cases:
        msg = str(case.args)
        if process_case:
            process_case(case)
        if process_args:
            process_args(case.args)

        actual = func(solution(), **case.args.__dict__)

        if process_result:
            actual = process_result(actual)

        if check_result:
            check_result(case, actual, msg)
        else:
            tst.assertEqual(case.expected, actual, msg=msg)


def test_invocations(tst, file, solution, process_case=None, process_args=None, process_result=None, check_result=None):
    cases = load_test_json(file).test_cases

    for case in cases:
        msg = str(case.args)
        if process_case:
            process_case(case)
        obj = None

        for func, parameters, expected in zip(case.functions, case.args, case.expected):
            if process_args:
                process_args(func, parameters)

            if func == solution.__name__:
                obj = solution(*parameters)
            else:
                actual = getattr(obj, func)(*parameters)

                if process_result:
                    actual = process_result(actual)

                if check_result:
                    check_result(expected, actual, msg)
                else:
                    tst.assertEqual(expected, actual, msg=msg)


def root_array_to_tree(args):
    args.root = TreeNode.from_array(args.root)


def linked_list_to_array(result):
    return ListNode.to_array(result)


def load_test_json(source_path):
    source_filename = os.path.splitext(os.path.basename(source_path))[0]
    prefix, problem_id, *_ = source_filename.split('_', 2)
    return load_json_from_path('../leetcode_test_cases/{}_{}.json'.format(prefix, problem_id))


def load_json_from_path(path):
    with open(path) as f:
        return json.load(f, object_hook=json_object_hook)


def json_object_hook(d):
    ref = d.pop('$ref', None)
    if ref is not None:
        d['_ref'] = ref

    obj_id = d.pop('$id', None)
    if obj_id is not None:
        d['_id'] = obj_id

    return types.SimpleNamespace(**d)


def solve_references(obj):
    JsonReferenceSolver(obj).solve(obj)


class JsonReferenceSolver:
    def __init__(self, obj):
        self.id_map = {}
        self.build_id_map(obj)

    def build_id_map(self, obj):
        if isinstance(obj, list):
            for v in obj:
                self.build_id_map(v)
        elif isinstance(obj, types.SimpleNamespace):
            obj_id = obj.__dict__.get('_id')
            if obj_id is not None:
                self.id_map[obj_id] = obj

            for k, v in obj.__dict__.items():
                self.build_id_map(v)

    def solve(self, obj):
        if isinstance(obj, list):
            for i, v in enumerate(obj):
                obj[i] = self.solve(v)
        elif isinstance(obj, types.SimpleNamespace):
            ref = obj.__dict__.get('_ref')
            if ref is not None:
                return self.id_map[ref]

            for k, v in obj.__dict__.items():
                obj.__dict__[k] = self.solve(v)

        return obj
