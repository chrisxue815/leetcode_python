import unittest
import collections
import random


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.indices = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        pool = self.indices[val]
        is_new_val = not pool
        pool.add(len(self.values))
        self.values.append(val)
        return is_new_val

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        pool = self.indices[val]
        if not pool:
            return False

        index = pool.pop()
        last = self.values.pop()

        if index != len(self.values):
            self.values[index] = last
            last_pool = self.indices[last] if last != val else pool
            last_pool.remove(len(self.values))
            last_pool.add(index)

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.values[random.randrange(len(self.values))]


class Test(unittest.TestCase):
    def test(self):
        rand_collection = RandomizedCollection()
        self.assertEqual(rand_collection.remove(1), False)
        self.assertEqual(rand_collection.insert(1), True)
        self.assertEqual(rand_collection.insert(1), False)
        self.assertEqual(rand_collection.insert(2), True)
        self.assertEqual(rand_collection.insert(2), False)
        self.assertEqual(rand_collection.insert(3), True)

        num_samples = 1000
        counter = collections.Counter(rand_collection.getRandom() for _ in xrange(num_samples))
        self.assertAlmostEqual(counter[1] / float(num_samples), 0.4, delta=0.01)

        self.assertEqual(rand_collection.remove(1), True)
        self.assertEqual(rand_collection.remove(1), True)
        self.assertEqual(rand_collection.remove(1), False)
        self.assertEqual(rand_collection.remove(3), True)
        self.assertEqual(rand_collection.remove(3), False)

        self.assertEqual(all(rand_collection.getRandom() == 2 for _ in xrange(num_samples)), True)


if __name__ == '__main__':
    unittest.main()
