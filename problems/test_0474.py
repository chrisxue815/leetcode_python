import unittest
from typing import List

import utils


# O(m * n * len(strs)) time. O(m * n * len(strs)) space. DP, 2D 0-1 knapsack.
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []
        for s in strs:
            zeros = sum(c == '0' for c in s)
            counts.append((zeros, len(s) - zeros))

        # dp[i][a][b]: the maximum number of strings in strs[:i] that you can form with given a 0s and b 1s
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]

        for i in range(1, len(strs) + 1):
            zeros, ones = counts[i - 1]
            for a in range(m + 1):
                for b in range(n + 1):
                    dp[i][a][b] = max(dp[i - 1][a][b], dp[i - 1][a - zeros][b - ones] + 1 if a >= zeros and b >= ones else 0)

        return dp[len(strs)][m][n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findMaxForm(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
