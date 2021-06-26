import unittest
from typing import List

import utils


# O(n) time. O(1) space. Iteration.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i in range(1, len(prices)):
            result += max(0, prices[i] - prices[i - 1])

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
