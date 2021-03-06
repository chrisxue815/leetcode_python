import unittest
from typing import List

import utils


# O(n) time. O(1) space. Space-optimized DP.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell1 = sell2 = 0
        buy1 = buy2 = -0x80000000

        for price in prices:
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)

        return sell2


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxProfit(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
