import unittest
import math
import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.orig = nums
        self.nums = list(nums)
        self.rand = random.Random()

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = self.nums
        for i in xrange(len(nums) - 1, -1, -1):
            j = self.rand.randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        return nums


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3])

    def _test(self, nums):
        solution = Solution(nums)

        iterations = 10000
        hits = 0
        for _ in xrange(iterations):
            arr = solution.shuffle()
            if arr == nums:
                hits += 1

        self.assertAlmostEqual(1.0 / math.factorial(len(nums)), float(hits) / iterations, places=2)


if __name__ == '__main__':
    unittest.main()
