import unittest

import utils


# O(n) time. O(n) space. DP.
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i]: the number of ways to decode s[:i+1]
        dp = [0] * len(s)

        for i in range(len(s)):
            if s[i] != '0':
                dp[i] = dp[i - 1] if i >= 1 else 1
            if i >= 1 and s[i - 1] != '0' and 1 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
