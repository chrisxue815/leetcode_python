import unittest
import utils


# O(nk) time. O(k) space. Iteration.
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

        buy = [-0x80000000] * k
        profit = [0] * k

        for price in prices:
            buy[0] = max(buy[0], -price)
            profit[0] = max(profit[0], buy[0] + price)

            for i in xrange(1, k):
                buy[i] = max(buy[i], profit[i - 1] - price)
                profit[i] = max(profit[i], buy[i] + price)

        return profit[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p188.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.k, case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
