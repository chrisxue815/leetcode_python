import unittest
from typing import List

import utils


# O(n) time. O(1) space. Space-optimized DP.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -0x80000000
        sell = prev_sell = 0

        for price in prices:
            curr_sell = sell
            sell = max(sell, buy + price)
            buy = max(buy, prev_sell - price)
            prev_sell = curr_sell

        return sell


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxProfit(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
