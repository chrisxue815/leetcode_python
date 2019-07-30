import unittest
from typing import List

import utils


# O(n^2) time. O(n^2) space. DP.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j]: how much more scores does player 1 get from nums[i:j] than player 2
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j - 1] - dp[i][j - 1])

        return dp[0][n] >= 0


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().PredictTheWinner(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
