import unittest
import utils


# O(n^2) time. O(n) space. DP.
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort()

        # dp[j]: Length of the longest pair chain in pairs[0:i+1] that contains pairs[j]
        dp = [1] * len(pairs)

        for i in range(len(pairs)):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1 if pairs[j][1] < pairs[i][0] else dp[j])

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().findLongestChain(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
