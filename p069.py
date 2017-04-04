import unittest


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo = 0
        hi = x
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_square = mid * mid
            if mid_square < x:
                lo = mid + 1
            elif mid_square > x:
                hi = mid - 1
            else:
                return mid

        return hi


class Test(unittest.TestCase):
    def test(self):
        self._test(0, 0)
        self._test(1, 1)
        self._test(2, 1)
        self._test(3, 1)
        self._test(4, 2)

    def _test(self, x, expected):
        actual = Solution().mySqrt(x)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
