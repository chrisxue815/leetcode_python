import unittest
import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((math.sqrt(8 * n + 1) - 1) / 2)


class Test(unittest.TestCase):
    def test(self):
        self._test(5, 2)
        self._test(8, 3)

    def _test(self, n, expected):
        actual = Solution().arrangeCoins(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
