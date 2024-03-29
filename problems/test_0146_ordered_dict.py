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
        utils.test_invocations(self, __file__, LRUCache)


if __name__ == '__main__':
    unittest.main()
