import unittest
import utils


# O(n^2) time. O(n) space. DP.
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # dp[j]: Maximum ASCII sum of common subsequnce of s1[:i] and s2[:j]
        dp = [0] * (len(s2) + 1)

        for i in xrange(1, len(s1) + 1):
            prev = 0
            for j in xrange(1, len(s2) + 1):
                curr = dp[j]
                if s1[i - 1] == s2[j - 1]:
                    dp[j] = prev + ord(s1[i - 1])
                else:
                    dp[j] = max(curr, dp[j - 1])
                prev = curr

        return sum(ord(ch) for s in [s1, s2] for ch in s) - dp[-1] * 2


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minimumDeleteSum(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
