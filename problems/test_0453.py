import unittest


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], 3)
        self._test([0, 0, 0], 0)
        self._test([-1, 1], 2)

    def _test(self, nums, expected):
        actual = Solution().minMoves(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
