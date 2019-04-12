import unittest
import utils


# O(n^2) time. O(n) space. DP.
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[j]: Length of longest common subsequence of word1[:i] and word2[:j]
        dp = [0] * (len(word2) + 1)

        for i in range(1, len(word1) + 1):
            prev = 0
            for j in range(1, len(word2) + 1):
                curr = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(curr, dp[j - 1])
                prev = curr

        return len(word1) + len(word2) - dp[-1] * 2


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minDistance(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
