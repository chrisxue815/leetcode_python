import unittest
import utils


# O(n^2) time. O(n^2) space. DP.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Is palindrome?
        dp = [[False] * len(s) for _ in xrange(len(s))]
        result = len(s)

        for distance in xrange(1, len(s)):
            for p in xrange(len(s) - distance):
                q = p + distance
                if s[p] == s[q] and (distance <= 2 or dp[p + 1][q - 1]):
                    dp[p][q] = True
                    result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p647.json').test_cases

        for case in cases:
            actual = Solution().countSubstrings(case.s)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()