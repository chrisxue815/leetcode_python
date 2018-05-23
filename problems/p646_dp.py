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

        for i in xrange(len(pairs)):
            for j in xrange(i):
                dp[i] = max(dp[i], dp[j] + 1 if pairs[j][1] < pairs[i][0] else dp[j])

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p646.json').test_cases

        for case in cases:
            actual = Solution().findLongestChain(case.pairs)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
