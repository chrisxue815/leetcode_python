import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = -0x80000000
        profit1 = profit2 = 0

        for price in prices:
            buy1 = max(buy1, -price)
            profit1 = max(profit1, buy1 + price)
            buy2 = max(buy2, profit1 - price)
            profit2 = max(profit2, buy2 + price)

        return profit2


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p123.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
