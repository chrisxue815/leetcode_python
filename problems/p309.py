import unittest
import utils


# O(n) time. O(n) space. DP.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        buy = [0] * len(prices)
        sell = [0] * len(prices)

        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, buy[0] + prices[1])

        for i in xrange(2, len(prices)):
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return sell[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p309.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
