import unittest
from typing import List

import utils


# O(n^3) time. O(n^2) space. DP.
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                multiplier = nums[i] * nums[j]
                dp[i][j] = max(nums[k] * multiplier + dp[i][k] + dp[k][j] for k in range(i + 1, j))

        return dp[0][-1]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
