import unittest


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.end)
        prev = intervals[0].end
        count = 1

        for curr in intervals:
            if curr.start >= prev:
                count += 1
                prev = curr.end

        return len(intervals) - count


class Test(unittest.TestCase):
    def test(self):
        self._test([[1, 2], [2, 3], [3, 4], [1, 3]], 1)
        self._test([[1, 2], [1, 2], [1, 2]], 2)
        self._test([[1, 2], [2, 3]], 0)

    def _test(self, intervals, expected):
        intervals = [Interval(start, end) for start, end in intervals]
        actual = Solution().eraseOverlapIntervals(intervals)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
