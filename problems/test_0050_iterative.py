import unittest


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if not x:
            return 0

        if n < 0:
            pos = False
            n = -n
        else:
            pos = True

        result = 1

        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result if pos else 1.0 / result


class Test(unittest.TestCase):
    def test(self):
        self._test(2, -2, 0.25)
        self._test(2, -1, 0.5)
        self._test(2, 0, 1)
        self._test(2, 1, 2)
        self._test(2, 2, 4)
        self._test(2, 3, 8)
        self._test(2, 4, 16)
        self._test(2, 5, 32)
        self._test(0, 1, 0)
        self._test(0, 0, 1)
        self._test(-2, 2, 4)
        self._test(-2, 3, -8)

    def _test(self, x, n, expected):
        actual = Solution().myPow(x, n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
