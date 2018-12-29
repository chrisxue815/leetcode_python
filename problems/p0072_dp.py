import unittest
import utils


# O(mn) time. O(mn) space. DP.
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j]: edit distance between word1[:i] and word2[:j]
        dp = [[0] * (len(word2) + 1) for _ in xrange(len(word1) + 1)]

        for i in xrange(len(word1) + 1):
            dp[i][0] = i

        for j in xrange(len(word2) + 1):
            dp[0][j] = j

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minDistance(case.word1, case.word2)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
