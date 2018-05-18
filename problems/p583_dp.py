import unittest
import utils


# O(n^2) time. O(n^2) space. DP.
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j]: Length of longest common subsequence of word1[:i+1] and word2[:j+1]
        dp = [[0] * len(word2) for _ in xrange(len(word1))]
        result = 0

        for i in xrange(len(word1)):
            for j in xrange(len(word2)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i >= 1 and j >= 1 else 1
                    result = max(result, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j - 1] if j >= 1 else 0, dp[i - 1][j] if i >= 1 else 0)

        return len(word1) + len(word2) - result * 2


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p583.json').test_cases

        for case in cases:
            actual = Solution().minDistance(case.word1, case.word2)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
