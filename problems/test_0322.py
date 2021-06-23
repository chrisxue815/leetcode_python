import unittest
from typing import List

import utils


# O(len(coins) * amount) time. O(amount) space. Space-optimized DP, unbounded knapsack.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_num_coins = amount + 1

        # dp[j]: the fewest number of coins you need in coins[:i] to make up amount j
        dp = [max_num_coins] * max_num_coins
        dp[0] = 0

        for coin in coins:
            for j in range(coin, max_num_coins):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[amount] if dp[amount] < max_num_coins else -1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
