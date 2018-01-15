import unittest


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) >> 1]
        return sum(abs(median - num) for num in nums)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], 2)
        self._test([0, 0, 0], 0)
        self._test([-1, 1], 2)
        self._test([1, 0, 0, 8, 6], 14)
        self._test([1, 0, 8, 6], 13)

    def _test(self, nums, expected):
        actual = Solution().minMoves2(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
