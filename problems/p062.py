import unittest
import utils


# O(mn) time. O(mn) space. DP.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[i][j]: the number of unique paths to reach (i, j)
        dp = [[1] * n for _ in xrange(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p062.json').test_cases

        for case in cases:
            actual = Solution().uniquePaths(case.m, case.n)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
