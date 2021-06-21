import unittest
from typing import List

import utils


# O(m * n * len(strs)) time. O(m * n) space. Space-optimized DP, 2D 0-1 knapsack.
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[a][b]: the maximum number of strings in strs[:i] that you can form with given a 0s and b 1s
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = sum(c == '0' for c in s)
            ones = len(s) - zeros

            for a in range(m, zeros - 1, -1):
                for b in range(n, ones - 1, -1):
                    dp[a][b] = max(dp[a][b], dp[a - zeros][b - ones] + 1)

        return dp[m][n]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
