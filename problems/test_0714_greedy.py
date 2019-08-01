import unittest
from typing import List

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        lo = 0x7FFFFFFF

        for price in prices:
            if price < lo:
                lo = price
            else:
                profit = price - lo - fee
                if profit > 0:
                    result += profit
                    lo = price - fee

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxProfit(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
