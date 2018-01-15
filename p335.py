import unittest


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        b = c = d = e = f = 0
        for a in x:
            if d >= b > 0 and (a >= c or c >= e and a >= c - e and f >= d - b):
                return True
            b, c, d, e, f = a, b, c, d, e

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 1, 1, 2], True)

        self._test([1, 2, 3, 4], False)

        self._test([1, 1, 1, 1], True)

        self._test([1, 2, 3, 8, 2, 2, 1], False)
        self._test([1, 2, 3, 8, 2, 2, 2], True)
        self._test([1, 2, 3, 8, 2, 2, 3], True)

        self._test([3, 3, 4, 2, 2], False)

    def _test(self, x, expected):
        actual = Solution().isSelfCrossing(x)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
