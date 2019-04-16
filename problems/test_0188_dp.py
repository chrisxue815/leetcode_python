import unittest
import utils


# O(nk) time. O(k) space. Space-optimized DP.
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
            for i in range(1, len(prices)):
                result += max(0, prices[i] - prices[i - 1])
            return result

        sell = [0] * (k + 1)
        buy = [-0x80000000] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                sell[i] = max(sell[i], buy[i] + price)
                buy[i] = max(buy[i], sell[i - 1] - price)

        return sell[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().maxProfit(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
