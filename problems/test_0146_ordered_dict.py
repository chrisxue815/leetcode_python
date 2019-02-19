import collections
import unittest

import utils


# O(1) time. O(n) space. Hash table, linked list.
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        val = self.cache.get(key)
        if val is None:
            return -1

        self.cache.move_to_end(key)

        return val

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class Test(unittest.TestCase):
    def test(self):
        cls = LRUCache
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
