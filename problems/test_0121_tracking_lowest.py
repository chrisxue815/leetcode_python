import unittest
from typing import List

import utils


# O(n) time. O(1) space. Iteration, tracking lowest value so far.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest = 0x7fffffff

        for price in prices:
            result = max(result, price - lowest)
            lowest = min(lowest, price)

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
