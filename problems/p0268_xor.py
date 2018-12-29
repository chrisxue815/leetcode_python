import unittest


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i, num in enumerate(nums):
            n ^= i ^ num
        return n


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 3], 2)
        self._test([0, 1, 2], 3)

    def _test(self, nums, expected):
        actual = Solution().missingNumber(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
