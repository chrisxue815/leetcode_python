import heapq
import unittest

import utils


# O(n) space. Binary heap.
class MedianFinder:

    # O(1) time.
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    # O(log(n)) time.
    def addNum(self, num: int) -> None:
        small = self.small
        large = self.large
        if len(small) == len(large):
            heapq.heappush(large, -heapq.heappushpop(small, -num))
        else:
            heapq.heappush(small, -heapq.heappushpop(large, num))

    # O(1) time.
    def findMedian(self) -> float:
        small = self.small
        large = self.large
        if len(small) == len(large):
            return (large[0] - small[0]) / 2
        else:
            return float(large[0])


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MedianFinder)


if __name__ == '__main__':
    unittest.main()
