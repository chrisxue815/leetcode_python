import unittest

import utils

CAPACITY = 10103


class Entry:
    def __init__(self, h, key, value, n):
        self.h = h  # hash
        self.key = key
        self.value = value
        self.n = n  # next


class MyHashMap:
    def __init__(self):
        self.table = [None] * CAPACITY

    def put(self, key: int, value: int) -> None:
        h = hash(key)
        bucket_index = h % CAPACITY
        curr = self.table[bucket_index]
        last = None

        while curr:
            if curr.h == h and curr.key == key:
                curr.value = value
                return
            last = curr
            curr = curr.n

        curr = Entry(h, key, value, None)

        if last:
            last.n = curr
        else:
            self.table[bucket_index] = curr

    def get(self, key: int) -> int:
        h = hash(key)
        bucket_index = h % CAPACITY
        curr = self.table[bucket_index]

        while curr:
            if curr.h == h and curr.key == key:
                return curr.value
            curr = curr.n

        return -1

    def remove(self, key: int) -> None:
        h = hash(key)
        bucket_index = h % CAPACITY
        curr = self.table[bucket_index]
        last = None

        while curr:
            if curr.h == h and curr.key == key:
                if last:
                    last.n = curr.n
                else:
                    self.table[bucket_index] = curr.n
                return

            last = curr
            curr = curr.n


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MyHashMap)


if __name__ == '__main__':
    unittest.main()
