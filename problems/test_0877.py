import unittest
from typing import List

import utils


# O(n^2) time. O(n^2) space. DP, minimax.
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j]: the largest number of stones you can get more than your opponent when picking piles[i:j+1]
        dp = [[0] * n for _ in range(n)]

        for i, pile in enumerate(piles):
            dp[i][i] = pile

        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])

        return dp[0][-1] > 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
