import unittest
from typing import List

import utils


# O(D * len(weights)) time. O(D * len(weights)) space. DP, TLE.
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # dp[i][j]: the least weight capacity required to ship weights[:j] within i days
        dp = [[0] * (len(weights) + 1) for _ in range(D + 1)]

        for j, weight in enumerate(weights):
            dp[1][j + 1] = dp[1][j] + weight

        for i in range(2, D + 1):
            for j in range(i - 1, len(weights) + 1):
                mini_max = 0x7fffffff

                for k in range(i - 1, j):
                    max_sum = max(dp[i - 1][k], dp[1][j] - dp[1][k])
                    if max_sum <= mini_max:
                        mini_max = max_sum
                    else:
                        break

                dp[i][j] = mini_max

        return dp[D][len(weights)]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shipWithinDays(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
