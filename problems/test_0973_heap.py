import heapq
import unittest
from typing import List

import utils


# O(nlog(k)) time. O(k) space. Binary heap.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for x, y in points:
            distance_squared = x * x + y * y

            if len(q) < k:
                heapq.heappush(q, (-distance_squared, x, y))
            elif distance_squared < -q[0][0]:
                heapq.heapreplace(q, (-distance_squared, x, y))

        return [it[1:] for it in q]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        self.assertCountEqual(case.expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
