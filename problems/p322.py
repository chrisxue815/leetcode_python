import unittest
import utils


# O(nm) time. O(m) space. Space-optimized DP.
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_num_coins = amount + 1
        dp = [max_num_coins] * max_num_coins
        dp[0] = 0

        for coin in coins:
            for curr_amount in xrange(coin, amount + 1):
                dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)

        return dp[-1] if dp[-1] < max_num_coins else -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p322.json').test_cases

        for case in cases:
            actual = Solution().coinChange(case.coins, case.amount)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
