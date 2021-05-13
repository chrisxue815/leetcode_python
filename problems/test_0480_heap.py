import heapq
import unittest
from typing import List

import utils


# O(nlog(k)) time. O(k) space. Heap.
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []
        large = []

        for i in range(k):
            heapq.heappush(large, (nums[i], i))
        for _ in range(k >> 1):
            move(large, small)

        result = [get_median(small, large, k)]

        for hi in range(k, len(nums)):
            lo = hi - k
            x = nums[hi]

            if x >= large[0][0]:
                heapq.heappush(large, (x, hi))
                if nums[lo] <= large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-x, hi))
                if nums[lo] >= large[0][0]:
                    move(small, large)

            while small and small[0][1] <= lo:
                heapq.heappop(small)
            while large and large[0][1] <= lo:
                heapq.heappop(large)

            result.append(get_median(small, large, k))

        return result


def move(h1, h2):
    x, i = heapq.heappop(h1)
    heapq.heappush(h2, (-x, i))


def get_median(h1, h2, k):
    return float(h2[0][0]) if k & 1 else (h2[0][0] - h1[0][0]) / 2


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
