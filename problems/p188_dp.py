import unittest
import utils


# O(nk) time. O(nk) space. DP.
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0 or len(prices) < 2:
            return 0

        if k * 2 >= len(prices):
            result = 0
            prev = prices[0]
            for price in prices:
                if price > prev:
                    result += price - prev
                prev = price
            return result

        # dp[i][j]: the maximal profit by completing at most i transactions in prices[0: j + 1]
        dp = [[0] * len(prices) for _ in xrange(k + 1)]

        for i in xrange(1, k + 1):
            max_profit = -prices[0]  # The max profit of one more transaction
            for j in xrange(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], max_profit + prices[j])
                max_profit = max(max_profit, dp[i - 1][j] - prices[j])

        return dp[k][-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p188.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.k, case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
