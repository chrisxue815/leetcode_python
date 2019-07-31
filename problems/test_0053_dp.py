import unittest
from typing import List

import utils


# O(n) time. O(n) space. Kadane's algorithm, DP.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i]: the maximum subarray that ends at i
        dp = [0] * len(nums)
        dp[0] = max_so_far = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            max_so_far = max(max_so_far, dp[i])

        return max_so_far


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxSubArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
