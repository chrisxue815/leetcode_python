import unittest
import utils


# O(n) time. O(n) space. DP.
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp[i]: minimum cost to reach i-th floor
        dp = [0] * (len(cost) + 1)

        for i in xrange(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minCostClimbingStairs(case.cost)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
