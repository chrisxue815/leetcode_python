import unittest


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = 0
        buy_price = prices[0]
        prev_price = prices[0]

        for price in prices[1:]:
            if price < prev_price:
                profit += prev_price - buy_price
                buy_price = price
            prev_price = price

        profit += prev_price - buy_price

        return profit


class Test(unittest.TestCase):
    def test(self):
        self._test([7, 1, 5, 3, 6, 4, 5], 8)
        self._test([7, 6, 4, 3, 1], 0)

    def _test(self, prices, expected):
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
