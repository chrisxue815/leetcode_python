import unittest


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n - 1))


class Test(unittest.TestCase):
    def test(self):
        self._test(-1, False)
        self._test(0, False)
        self._test(1, True)
        self._test(2, True)
        self._test(3, False)
        self._test(4, True)

    def _test(self, n, expected):
        actual = Solution().isPowerOfTwo(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
