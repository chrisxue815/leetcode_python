import unittest
import utils


# O(n) time. O(n) space. DP.
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            raise ValueError('Expected n >= 0. Got n = {}'.format(n))
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        # dp[i]: fib(i)
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().fib(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
