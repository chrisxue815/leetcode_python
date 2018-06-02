import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = 0x7FFFFFFF
        profit1 = profit2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p123.json').test_cases

        for case in cases:
            actual = Solution().maxProfit(case.prices)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
