import unittest
from typing import List

import utils

MAX_INT = 0x7fffffff


# O(len(coins) * amount) time. O(amount) space. Space-optimized DP, unbounded knapsack.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[j]: the fewest number of coins you need in coins[:i] to make up amount j
        dp = [MAX_INT] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(coins) + 1):
            for j in range(coins[i - 1], amount + 1):
                num = dp[j - coins[i - 1]]
                if num != MAX_INT:
                    dp[j] = min(dp[j], num + 1)

        return dp[amount] if dp[amount] != MAX_INT else -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().coinChange(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
