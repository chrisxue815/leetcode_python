import unittest
import collections
import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.indices = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        index = self.indices.pop(val, None)
        if index is None:
            return False
        last = self.values.pop()
        if index < len(self.values):
            self.values[index] = last
            self.indices[last] = index
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.values[random.randrange(len(self.values))]


class Test(unittest.TestCase):
    def test(self):
        rand_set = RandomizedSet()
        self.assertEqual(True, rand_set.insert(1))
        self.assertEqual(False, rand_set.remove(2))
        self.assertEqual(True, rand_set.insert(2))

        num_samples = 10000
        counter = collections.Counter(rand_set.getRandom() for _ in range(num_samples))
        self.assertAlmostEqual(counter[1] / float(num_samples), 0.5, delta=0.05)

        self.assertEqual(True, rand_set.remove(1))
        self.assertEqual(False, rand_set.insert(2))

        self.assertEqual(True, all(rand_set.getRandom() == 2 for _ in range(num_samples)))


if __name__ == '__main__':
    unittest.main()
