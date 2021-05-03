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
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
