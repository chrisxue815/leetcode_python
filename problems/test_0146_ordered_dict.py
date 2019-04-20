import collections
import unittest

import utils


# O(capacity) space. Hash table, linked list, ordered dict.
class LRUCache:
    # O(1) time. O(1) space.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # O(1) time. O(1) space.
    def get(self, key: int) -> int:
        val = self.cache.get(key)
        if val is None:
            return -1

        self.cache.move_to_end(key)

        return val

    # O(1) time. O(1) space.
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
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
