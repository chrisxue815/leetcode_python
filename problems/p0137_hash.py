import unittest
import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 3, 3, 1, 5, 5, 5], 1)

    def _test(self, nums, expected):
        actual = Solution().singleNumber(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()