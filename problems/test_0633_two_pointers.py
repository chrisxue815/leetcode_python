import unittest
import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        lo = 0
        hi = int(math.sqrt(c))

        while lo <= hi:
            d = lo * lo + hi * hi
            if d < c:
                lo += 1
            elif d > c:
                hi -= 1
            else:
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test(5, True)
        self._test(3, False)

    def _test(self, nums, expected):
        actual = Solution().judgeSquareSum(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
