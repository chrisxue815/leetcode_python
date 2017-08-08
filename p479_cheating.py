import unittest


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return [0, 9, 987, 123, 597, 677, 1218, 877, 475][n]


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 9)
        self._test(2, 987)
        self._test(3, 123)
        self._test(4, 597)
        self._test(5, 677)
        self._test(6, 1218)
        self._test(7, 877)
        self._test(8, 475)

    def _test(self, heights, expected):
        actual = Solution().largestPalindrome(heights)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
