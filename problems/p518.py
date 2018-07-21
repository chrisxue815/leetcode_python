import unittest
import utils


# O(n*m) time. O(n*m) space. DP.
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0] * (amount + 1) for _ in xrange(len(coins) + 1)]
        dp[0][0] = 1

        for i in xrange(1, len(coins) + 1):
            coin = coins[i - 1]
            for j in xrange(coin):
                combinations = 0
                for k in xrange(j, amount + 1, coin):
                    combinations += dp[i - 1][k]
                    dp[i][k] = combinations

        return dp[-1][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p518.json').test_cases

        for case in cases:
            actual = Solution().change(case.amount, case.coins)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
