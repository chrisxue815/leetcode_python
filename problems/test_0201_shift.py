import unittest


class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift


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
