import unittest


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        m = 1
        while m <= n:
            m2 = m * 10
            result += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m = m2
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(13, 6)
        self._test(1, 1)
        self._test(10, 2)
        self._test(11, 4)

    def _test(self, n, expected):
        actual = Solution().countDigitOne(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
