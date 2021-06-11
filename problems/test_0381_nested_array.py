import collections
import random
import unittest


class RandomizedCollection:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.indices = collections.defaultdict(list)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        pool = self.indices[val]
        is_new_val = not pool
        pool.append(len(self.values))
        self.values.append((val, len(pool) - 1))
        return is_new_val

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        pool = self.indices[val]
        if not pool:
            return False

        index = pool.pop()
        last, last_index = self.values.pop()

        if index != len(self.values):
            self.values[index] = (last, last_index)
            last_pool = self.indices[last] if last != val else pool
            last_pool[last_index] = index

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.values[random.randrange(len(self.values))][0]


class Test(unittest.TestCase):
    def test(self):
        rand_collection = RandomizedCollection()
        self.assertEqual(False, rand_collection.remove(1))
        self.assertEqual(True, rand_collection.insert(1))
        self.assertEqual(False, rand_collection.insert(1))
        self.assertEqual(True, rand_collection.insert(2))
        self.assertEqual(False, rand_collection.insert(2))
        self.assertEqual(True, rand_collection.insert(3))

        num_samples = 10000
        counter = collections.Counter(rand_collection.getRandom() for _ in range(num_samples))
        self.assertAlmostEqual(counter[1] / float(num_samples), 0.4, delta=0.01)

        self.assertEqual(True, rand_collection.remove(1))
        self.assertEqual(True, rand_collection.remove(1))
        self.assertEqual(False, rand_collection.remove(1))
        self.assertEqual(True, rand_collection.remove(3))
        self.assertEqual(False, rand_collection.remove(3))

        self.assertEqual(True, all(rand_collection.getRandom() == 2 for _ in range(num_samples)))


if __name__ == '__main__':
    unittest.main()
