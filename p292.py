import unittest


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0


class Test(unittest.TestCase):
    def test(self):
        self._test(1, True)
        self._test(2, True)
        self._test(3, True)
        self._test(4, False)
        self._test(5, True)
        self._test(6, True)
        self._test(7, True)
        self._test(8, False)

    def _test(self, n, expected):
        actual = Solution().canWinNim(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
