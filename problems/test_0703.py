import heapq
import unittest
from typing import List

import utils


# O(log(k)) time. O(k) space. Binary heap.
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        k_largest = []

        for num in nums[:k]:
            heapq.heappush(k_largest, num)

        for num in nums[k:]:
            heapq.heappushpop(k_largest, num)

        self.k_largest = k_largest
        self.k = k

    def add(self, val: int) -> int:
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
        else:
            heapq.heappushpop(self.k_largest, val)

        return self.k_largest[0]


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, KthLargest)


if __name__ == '__main__':
    unittest.main()
