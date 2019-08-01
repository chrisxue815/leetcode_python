import unittest

import utils


# O(n) time. O(n) space. DP.
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i]: In how many distinct ways can you climb to the i-th floor (0-based)?
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().climbStairs(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
