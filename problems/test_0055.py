import unittest


# O(n). Linear iteration
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hi = 0
        for lo, num in enumerate(nums):
            if lo > hi:
                return False
            hi = max(hi, lo + num)
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 3, 1, 1, 4], True)
        self._test([3, 2, 1, 0, 4], False)

    def _test(self, nums, expected):
        actual = Solution().canJump(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
