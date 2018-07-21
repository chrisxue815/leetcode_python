import unittest
import utils


# O(n*m) time. O(m) space. Space-optimized DP.
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in xrange(coin, amount + 1):
                dp[j] += dp[j - coin]

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p518.json').test_cases

        for case in cases:
            actual = Solution().change(case.amount, case.coins)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
