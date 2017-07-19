import unittest
import itertools


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # TODO: binary search left and right index to merge into newInterval
        for i, old in enumerate(intervals):
            if newInterval.start <= old.end:
                if newInterval.end < old.start:
                    intervals.insert(i, newInterval)
                    return intervals
                else:
                    old.start = min(old.start, newInterval.start)
                    old.end = max(old.end, newInterval.end)
                    lo, lo_interval = i, old
                    break
        else:
            intervals.append(newInterval)
            return intervals

        for hi_index, hi_interval in enumerate(itertools.islice(intervals, lo + 1, len(intervals))):
            if hi_interval.start <= lo_interval.end:
                lo_interval.end = max(lo_interval.end, hi_interval.end)
            else:
                intervals[lo + 1:] = intervals[lo + 1 + hi_index:]
                return intervals

        return intervals[:lo + 1]


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]])

        self._test(
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 9],
            [[1, 2], [3, 10], [12, 16]])

    def _test(self, intervals, newInterval, expected):
        intervals = [Interval(*interval) for interval in intervals]
        newInterval = Interval(*newInterval)

        actual = Solution().insert(intervals, newInterval)

        actual = [[interval.start, interval.end] for interval in actual]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
