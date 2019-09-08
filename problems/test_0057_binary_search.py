import bisect
import unittest
from typing import List

import utils


class KeyedSequence:
    def __init__(self, sequence, key_func):
        self.sequence = sequence
        self.key_func = key_func

    def __getitem__(self, i):
        return self.key_func(self.sequence[i])

    def __len__(self):
        return len(self.sequence)


# O(log(n)) time. O(1) space. Interval, binary search, in-place.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        starts = KeyedSequence(intervals, lambda interval: interval[0])
        ends = KeyedSequence(intervals, lambda interval: interval[1])

        left = bisect.bisect_left(ends, newInterval[0])
        right = bisect.bisect_right(starts, newInterval[1], lo=left)

        if left == right:
            intervals.insert(left, newInterval)
        else:
            intervals[left][0] = min(intervals[left][0], newInterval[0])
            intervals[left][1] = max(intervals[right - 1][1], newInterval[1])
            del intervals[left + 1:right]

        return intervals


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().insert(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
