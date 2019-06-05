import unittest
from typing import List

import utils


# O(n * sum(nums)) time. O(sum(nums)) space. Space-optimized DP, 0-1 knapsack.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        target = s >> 1

        # dp[j]: can you add up some elements in nums[:i] to get sum j?
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

            if dp[target]:
                return True

        return dp[target]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().canPartition(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
