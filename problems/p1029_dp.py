import unittest

import utils


# O(n^2) time. O(n^2) space. DP.
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        m = len(costs)
        n = m // 2

        # dp[i][j]: minimal cost to fly i people to A, j people to B, for costs[:i+j]
        dp = [[0] * m for _ in xrange(m)]

        for i in xrange(1, m):
            dp[i][0] = dp[i - 1][0] + costs[i - 1][0]
            dp[0][i] = dp[0][i - 1] + costs[i - 1][1]

        for i in xrange(1, n + 1):
            for j in xrange(1, n + 1):
                dp[i][j] = min(dp[i - 1][j] + costs[i + j - 1][0], dp[i][j - 1] + costs[i + j - 1][1])

        return dp[n][n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().twoCitySchedCost(case.costs)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
