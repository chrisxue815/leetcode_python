import unittest

import utils


# O(n^2) time. O(n^2) space. DP.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # dp[i][j]: the longest palindromic subsequence's length in s[i:j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            dp[i][i + 1] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[j - 1] else max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().longestPalindromeSubseq(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
