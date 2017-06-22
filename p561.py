import unittest
import itertools


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        return sum(itertools.islice(nums, 0, len(nums), 2))


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 4, 3, 2], 4)
        self._test([1, 4, 3, 2, 6, 5], 9)

    def _test(self, nums, expected):
        actual = Solution().arrayPairSum(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
