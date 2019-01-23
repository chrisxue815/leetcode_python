import unittest
import utils


# O(n^2) time. O(n) space. Space-optimized DP.
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        # dp[i][j]: the minimum path sum to reach triangle[i][j]
        dp = [0] * n

        for i in xrange(n):
            prev = 0x7FFFFFFF

            for j in xrange(i + 1):
                curr = triangle[i][j]

                if i >= 1:
                    if j < i:
                        prev = min(prev, dp[j])
                    curr += prev

                prev = dp[j]
                dp[j] = curr

        return min(dp)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minimumTotal(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
