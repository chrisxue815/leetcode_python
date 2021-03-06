import unittest
from typing import List

import utils


# O(n) time. O(1) space. Kadane's algorithm.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = max_ending_here = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            max_ending_here = max(diff, max_ending_here + diff)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxProfit(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
