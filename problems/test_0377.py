import unittest
from typing import List

import utils


# O(target * len(nums)) time. O(target) space. DP, unbounded knapsack.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i]: the number of possible permutations that add up to i
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            dp[i] = sum(dp[i - num] for num in nums if i >= num)

        return dp[target]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().combinationSum4(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
