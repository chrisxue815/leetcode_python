import unittest
import math


class Solution:
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        max_m = int(math.log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n ** (1.0 / m))
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)


class Test(unittest.TestCase):
    def test(self):
        self._test('13', '3')
        self._test('4681', '8')
        self._test('1000000000000000000', '999999999999999999')

    def _test(self, n, expected):
        actual = Solution().smallestGoodBase(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
