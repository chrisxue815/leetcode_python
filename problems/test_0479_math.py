import math
import unittest

import utils


def reverse(num):
    result = 0
    while num > 0:
        num, r = divmod(num, 10)
        result = result * 10 + r
    return result


class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9

        for z in range(2, 9 * 10 ** (n - 1)):
            hi = 10 ** n - z
            lo = reverse(hi)

            # Discriminant
            # https://leetcode.com/problems/largest-palindrome-product/discuss/171580/Python-Solution-using-Math-and-Detailed-Mathematical-deduction
            d = z * z - 4 * lo
            if d < 0:
                continue

            sd = int(math.sqrt(d))
            if sd * sd == d:
                return (hi * 10 ** n + lo) % 1337


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().largestPalindrome(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
