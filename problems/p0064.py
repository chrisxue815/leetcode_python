import unittest
import utils


# O(mn) time. O(mn) space. DP.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # dp[i][j]: the minimal sum of path to reach (i, j)
        dp = [[0] * n for _ in xrange(m)]

        sum_ = 0
        for i in xrange(m):
            sum_ += grid[i][0]
            dp[i][0] = sum_

        sum_ = 0
        for j in xrange(n):
            sum_ += grid[0][j]
            dp[0][j] = sum_

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minPathSum(case.grid)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
