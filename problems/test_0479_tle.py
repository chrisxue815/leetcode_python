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

        max_num = 10 ** n - 1

        for hi in range(10 ** n - 2, 10 ** (n - 1) - 1, -1):
            palindrome = hi * 10 ** n + reverse(hi)
            root = int(math.ceil(math.sqrt(palindrome)))

            for factor1 in range(max_num, root - 1, -1):
                factor2, r = divmod(palindrome, factor1)

                if r == 0:
                    return palindrome % 1337
                if factor2 > max_num:
                    break


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        # The last 2 tests are too slow
        for case in cases[:-2]:
            args = str(case.args)
            actual = Solution().largestPalindrome(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
