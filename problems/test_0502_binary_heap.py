import heapq
import unittest
from typing import List

import utils


# O(klog(n)) time. O(n) space. Binary heap.
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_queue = []
        profit_queue = []

        for i, c in enumerate(capital):
            heapq.heappush(capital_queue, (c, i))

        for _ in range(k):
            while capital_queue and capital_queue[0][0] <= w:
                _, i = heapq.heappop(capital_queue)
                heapq.heappush(profit_queue, -profits[i])
            if not profit_queue:
                break
            profit = -heapq.heappop(profit_queue)
            w += profit

        return w


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
