import unittest

import utils


# O(n^2) time. O(n^2) space. DP.
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = float(poured)
        for r in range(query_row):
            for c in range(r + 1):
                p = dp[r][c]
                if p > 1.0:
                    p = (p - 1) / 2.0
                    dp[r + 1][c] += p
                    dp[r + 1][c + 1] += p

        return dp[query_row][query_glass] if dp[query_row][query_glass] < 1.0 else 1.0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
