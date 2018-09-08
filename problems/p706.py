import unittest
import utils

CAPACITY = 10103


class Entry(object):
    def __init__(self, h, key, value, n):
        self.h = h  # hash
        self.key = key
        self.value = value
        self.n = n  # next


class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * CAPACITY

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
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

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        h = hash(key)
        bucket_index = h % CAPACITY
        curr = self.table[bucket_index]

        while curr:
            if curr.h == h and curr.key == key:
                return curr.value
            curr = curr.n

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
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
        cases = utils.load_json_from_path('../leetcode_test_cases/p706.json').test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.parameters, case.expected):
                if func == 'MyHashMap':
                    obj = MyHashMap()
                if func == 'put':
                    actual = obj.put(*parameters)
                    self.assertEqual(expected, actual)
                elif func == 'remove':
                    actual = obj.remove(*parameters)
                    self.assertEqual(expected, actual)
                elif func == 'get':
                    actual = obj.get(*parameters)
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
