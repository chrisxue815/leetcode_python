import unittest
from typing import List

import utils


# O(n) time. O(1) space. Keeping the lowest price.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest_so_far = 0x7FFFFFFF

        for price in prices:
            result = max(result, price - lowest_so_far)
            lowest_so_far = min(lowest_so_far, price)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
