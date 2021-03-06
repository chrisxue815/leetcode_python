import unittest
import utils


# O(n^2) time. O(n^2) space. DP.
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Is palindrome?
        dp = [[False] * len(s) for _ in range(len(s))]
        result = len(s)

        for distance in range(1, len(s)):
            for p in range(len(s) - distance):
                q = p + distance
                if s[p] == s[q] and (distance <= 2 or dp[p + 1][q - 1]):
                    dp[p][q] = True
                    result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countSubstrings(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
