import unittest
from typing import List

import utils


# O(n) time. O(1) space. Space-optimized DP.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = -0x80000000

        for price in prices:
            sell = max(sell, buy + price)
            buy = max(buy, sell - price)

        return sell


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
