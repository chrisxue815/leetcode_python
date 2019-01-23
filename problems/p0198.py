import unittest
import utils


# O(n) time. O(n) space. DP.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        # dp[i]: the maximum amount of money you can rob from nums[0:i+1]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in xrange(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().rob(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
