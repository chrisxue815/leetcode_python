import unittest


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while n > m:
            n &= (n - 1)
        return n


class Test(unittest.TestCase):
    def test(self):
        self._test(5, 7, 4)
        self._test(1, 3, 0)
        self._test(5, 5, 5)
        self._test(10, 11, 10)

    def _test(self, m, n, expected):
        actual = Solution().rangeBitwiseAnd(m, n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
