import unittest
from typing import List

import utils


# O(len(nums) * (sum(nums) + max(nums))) time. O(len(nums) * (sum(nums) + max(nums))) space. DP, 0-1 knapsack.
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 1 if S == 0 else 0

        sum_ = sum(nums)
        if not (-sum_ <= S <= sum_):
            return 0

        max_ = max(nums)
        bound = sum_ + max_
        range_ = bound * 2 + 1

        # dp[i][j]: how many ways to assign symbols to make sum of nums[:i] equal to target j
        dp = [[0] * range_ for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(-sum_, sum_ + 1):
                dp[i][j] = dp[i - 1][j - num] + dp[i - 1][j + num]

        return dp[len(nums)][S]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findTargetSumWays(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
