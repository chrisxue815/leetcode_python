import unittest
import collections
import random


class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.indices = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        pool = self.indices[val]
        is_new_val = not pool
        pool.add(len(self.values))
        self.values.append(val)
        return is_new_val

    def remove(self, val: int) -> bool:
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

    def getRandom(self) -> int:
        return self.values[random.randrange(len(self.values))]


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
        self.assertAlmostEqual(counter[1] / float(num_samples), 0.4, delta=0.1)

        self.assertEqual(True, rand_collection.remove(1))
        self.assertEqual(True, rand_collection.remove(1))
        self.assertEqual(False, rand_collection.remove(1))
        self.assertEqual(True, rand_collection.remove(3))
        self.assertEqual(False, rand_collection.remove(3))

        self.assertEqual(True, all(rand_collection.getRandom() == 2 for _ in range(num_samples)))


if __name__ == '__main__':
    unittest.main()
