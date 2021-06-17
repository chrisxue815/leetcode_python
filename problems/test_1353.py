import heapq
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Greedy, binary heap.
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        result = 0
        d = 0
        q = []
        while events or q:
            if not q:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heapq.heappush(q, events.pop()[1])
            heapq.heappop(q)
            result += 1
            d += 1
            while q and q[0] < d:
                heapq.heappop(q)
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
