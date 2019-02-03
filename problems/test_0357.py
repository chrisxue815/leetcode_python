import unittest
import utils


# O(n) time. O(1) space. DP.
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if n == 0:
            return 1

        n = min(n, 10)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)

        return sum(dp)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().countNumbersWithUniqueDigits(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
