import unittest
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 3, 1], 3)

    def _test(self, nums, expected):
        actual = Solution().singleNumber(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
