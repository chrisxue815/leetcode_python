import unittest
import utils


# O(mn) time. O(mn) space. DP.
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # dp[i][j]: the number of unique paths to reach (i, j)
        dp = [[0] * n for _ in xrange(m)]

        for i in xrange(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in xrange(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().uniquePathsWithObstacles(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
