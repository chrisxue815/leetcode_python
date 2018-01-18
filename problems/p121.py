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
        largest = prices[0]
        smallest = prices[0]

        for price in prices[1:]:
            if largest < price:
                largest = price
            elif smallest > price:
                new_profit = largest - smallest
                if profit < new_profit:
                    profit = new_profit
                smallest = price
                largest = price

        return max(profit, largest - smallest)


class Test(unittest.TestCase):
    def test(self):
        self._test([7, 1, 5, 3, 6, 4], 5)
        self._test([7, 6, 4, 3, 1], 0)

    def _test(self, prices, expected):
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
