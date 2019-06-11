import unittest
from typing import List

import utils


# O(len(nums) * sum(nums)) time. O(len(nums) * sum(nums)) space. DP, 0-1 knapsack.
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_nums = sum(nums)
        if not (-sum_nums <= S <= sum_nums):
            return 0

        max_num = max(nums)

        # dp[i][j]: how many ways to assign symbols to make sum of nums[:i] equal to target j
        dp = [[0] * ((sum_nums + max_num) * 2 + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(-sum_nums - num, sum_nums + num + 1):
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
