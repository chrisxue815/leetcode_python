import unittest

import utils


# O(n^2) time. O(n^2) space. DP.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        max_lo = 0

        # dp[i][j]: is s[i:j] palindrome?
        dp = [[False] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][i] = True

        for i in range(n):
            dp[i][i + 1] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j - 1]

                if dp[i][j] and j - i > max_len:
                    max_len = j - i
                    max_lo = i

        return s[max_lo:max_lo + max_len]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().longestPalindrome(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
