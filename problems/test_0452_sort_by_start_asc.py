import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by start in ascending order, greedy.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()
        num_non_overlaps = 0
        prev_end = points[0][0] - 1

        for start, end in points:
            if prev_end < start:
                num_non_overlaps += 1
                prev_end = end
            else:
                prev_end = min(prev_end, end)

        return num_non_overlaps


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
