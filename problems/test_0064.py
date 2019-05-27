import unittest
import utils


# O(mn) time. O(mn) space. DP.
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # dp[i][j]: the minimal sum of path to reach (i, j)
        dp = [[0] * n for _ in range(m)]

        sum_ = 0
        for i in range(m):
            sum_ += grid[i][0]
            dp[i][0] = sum_

        sum_ = 0
        for j in range(n):
            sum_ += grid[0][j]
            dp[0][j] = sum_

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().minPathSum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
