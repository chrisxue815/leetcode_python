import unittest
from typing import List

import utils


# O(mn) time. O(mn) space. DP, TLE.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j, num in enumerate(nums):
            dp[1][j + 1] = dp[1][j] + num

        for i in range(2, m + 1):
            for j in range(n + 1):
                mini_max = 0x7fffffff

                for k in range(j):
                    mini_max = min(mini_max, max(dp[i - 1][k], dp[1][j] - dp[1][k]))

                dp[i][j] = mini_max

        return dp[m][n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().splitArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
