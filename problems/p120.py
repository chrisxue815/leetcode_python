import unittest
import utils


# O(n^2) time. O(n^2) space. DP.
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        # dp[i][j]: the minimum path sum to reach triangle[i][j]
        dp = [[0] * (i + 1) for i in xrange(n)]

        for i in xrange(n):
            for j in xrange(i + 1):
                dp[i][j] = triangle[i][j]

                if i >= 1:
                    prev = 0x7FFFFFFF
                    if j >= 1:
                        prev = dp[i - 1][j - 1]
                    if j < i:
                        prev = min(prev, dp[i - 1][j])
                    dp[i][j] += prev

        return min(dp[-1])


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p120.json').test_cases

        for case in cases:
            actual = Solution().minimumTotal(case.triangle)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
