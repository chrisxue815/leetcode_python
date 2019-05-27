import unittest


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        def search(num, find_left):
            lo = 0
            hi = len(intervals) - 1

            while lo <= hi:
                mid = lo + ((hi - lo) >> 1)
                mid_start = intervals[mid].end if find_left else intervals[mid].start
                if mid_start < num:
                    lo = mid + 1
                elif mid_start > num:
                    hi = mid - 1
                else:
                    return mid
            return lo if find_left else hi

        left = search(newInterval.start, True)
        right = search(newInterval.end, False)

        if left > right:
            intervals.insert(left, newInterval)
        else:
            left_interval = intervals[left]
            left_interval.start = min(left_interval.start, newInterval.start)
            left_interval.end = max(intervals[right].end, newInterval.end)
            del intervals[left + 1:right + 1]

        return intervals


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

        self._test(
            [[1, 3], [6, 9]],
            [0, 10],
            [[0, 10]])

        self._test(
            [],
            [5, 7],
            [[5, 7]]
        )

        self._test(
            [[1, 5]],
            [6, 8],
            [[1, 5], [6, 8]]
        )

        self._test(
            [[1, 3], [7, 9]],
            [5, 6],
            [[1, 3], [5, 6], [7, 9]]
        )

    def _test(self, intervals, newInterval, expected):
        intervals = [Interval(*interval) for interval in intervals]
        newInterval = Interval(*newInterval)

        actual = Solution().insert(intervals, newInterval)

        actual = [[interval.start, interval.end] for interval in actual]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
