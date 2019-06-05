import unittest
from typing import List

import utils


# O(n * sum(nums)) time. O(n * sum(nums)) space. DP, 0-1 knapsack.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        target = s >> 1

        # dp[i][j]: can you add up some elements in nums[:i] to get sum j?
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            dp[i - 1][0] = True

            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i - 1]] if j >= nums[i - 1] else False)

        return dp[len(nums)][target]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().canPartition(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
