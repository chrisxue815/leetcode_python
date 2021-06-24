import bisect
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. DP, sorting, binary search, interval.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        ends = [0]
        profits = [0]
        for end, start, profit in jobs:
            i = bisect.bisect(ends, start) - 1
            total_profit = profits[i] + profit
            if total_profit > profits[-1]:
                ends.append(end)
                profits.append(total_profit)
        return profits[-1]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
