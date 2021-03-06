import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by end, greedy.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[1])
        num_non_overlaps = 0
        prev_end = intervals[0][0] - 1

        for start, end in intervals:
            if prev_end <= start:
                num_non_overlaps += 1
                prev_end = end

        return len(intervals) - num_non_overlaps


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().eraseOverlapIntervals(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
