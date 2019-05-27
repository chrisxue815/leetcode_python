import unittest


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and not num & (num - 1) and not num & 0xaaaaaaaa


class Test(unittest.TestCase):
    def test(self):
        self._test(-1, False)
        self._test(0, False)
        self._test(1, True)
        self._test(2, False)
        self._test(3, False)
        self._test(4, True)
        self._test(5, False)

    def _test(self, n, expected):
        actual = Solution().isPowerOfFour(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
