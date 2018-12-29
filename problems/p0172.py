import unittest


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= 5:
            n //= 5
            result += n
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(-1, 0)
        self._test(0, 0)
        self._test(1, 0)
        self._test(5, 1)
        self._test(10, 2)
        self._test(25, 6)
        self._test(30, 7)
        self._test(50, 12)
        self._test(75, 18)
        self._test(92, 21)
        self._test(125, 31)

    def _test(self, n, expected):
        actual = Solution().trailingZeroes(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
