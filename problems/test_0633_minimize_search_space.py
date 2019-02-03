import unittest
import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(math.sqrt(c / 2)), int(math.sqrt(c)) + 1):
            if math.sqrt(c - a * a).is_integer():
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
