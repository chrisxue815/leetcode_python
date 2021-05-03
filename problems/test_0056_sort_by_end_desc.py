import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by end in descending order, greedy.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval[1], reverse=True)
        result = [intervals[0]]

        for interval in intervals:
            if interval[1] < result[-1][0]:
                result.append(interval)
            else:
                result[-1][0] = min(result[-1][0], interval[0])

        result.reverse()
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
