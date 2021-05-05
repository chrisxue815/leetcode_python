import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by start in ascending order, greedy.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        result = [intervals[0]]

        for interval in intervals:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, result_processor=lambda result: sorted(result))


if __name__ == '__main__':
    unittest.main()
