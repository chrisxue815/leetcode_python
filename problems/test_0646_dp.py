import unittest
from typing import List

import utils


# O(n^2) time. O(n) space. DP.
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        # dp[i]: Length of the longest pair chain in pairs[:i]
        dp = [1] * (len(pairs) + 1)
        dp[0] = 0

        for i in range(2, len(pairs) + 1):
            dp[i] = max(dp[j] + 1 if pairs[j - 1][1] < pairs[i - 1][0] else dp[j] for j in range(1, i))

        return dp[len(pairs)]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findLongestChain(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
