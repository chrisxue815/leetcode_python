import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by end in descending order, greedy.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda point: point[1], reverse=True)
        num_non_overlaps = 0
        prev_start = points[0][1] + 1

        for start, end in points:
            if end < prev_start:
                num_non_overlaps += 1
                prev_start = start
            else:
                prev_start = max(prev_start, start)

        return num_non_overlaps


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
