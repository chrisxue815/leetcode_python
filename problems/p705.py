import unittest
import utils

CAPACITY = 10103


class Entry(object):
    def __init__(self, h, key, n):
        self.h = h  # hash
        self.key = key
        self.n = n  # next


class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * CAPACITY

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        h = hash(key)
        bucket_index = h % CAPACITY
        curr = self.table[bucket_index]
        last = None

        while curr:
            if curr.h == h and curr.key == key:
                return

            last = curr
            curr = curr.n

        curr = Entry(h, key, None)

        if last:
            last.n = curr
        else:
            self.table[bucket_index] = curr

    def remove(self, key):
        """
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

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = hash(key)
        bucket_index = h % CAPACITY
        curr = self.table[bucket_index]

        while curr:
            if curr.h == h and curr.key == key:
                return True
            curr = curr.n

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p705.json').test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.parameters, case.expected):
                if func == 'MyHashSet':
                    obj = MyHashSet()
                if func == 'add':
                    actual = obj.add(*parameters)
                    self.assertEqual(expected, actual)
                elif func == 'remove':
                    actual = obj.remove(*parameters)
                    self.assertEqual(expected, actual)
                elif func == 'contains':
                    actual = obj.contains(*parameters)
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
