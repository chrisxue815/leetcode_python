import unittest
import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        sum_ = 1
        sqrt = int(math.sqrt(num))

        for divisor in xrange(2, sqrt + 1):
            if not num % divisor:
                sum_ += divisor + num // divisor

        return sum_ == num


class Test(unittest.TestCase):
    def test(self):
        self._test(28, True)
        self._test(1, False)
        self._test(0, False)
        self._test(-1, False)

    def _test(self, num, expected):
        actual = Solution().checkPerfectNumber(num)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
