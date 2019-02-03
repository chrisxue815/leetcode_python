import sys
import unittest


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        result = []
        for i in range(len(intervals)):
            min_index = -1
            min_val = sys.maxsize
            for j in range(len(intervals)):
                if i == j:
                    continue
                if intervals[i].end <= intervals[j].start < min_val:
                    min_index = j
                    min_val = intervals[j].start

            result.append(min_index)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([[1, 2]], [-1])
        self._test([[3, 4], [2, 3], [1, 2]], [-1, 0, 1])
        self._test([[1, 4], [2, 3], [3, 4]], [-1, 2, -1])

    def _test(self, intervals, expected):
        intervals = [Interval(a[0], a[1]) for a in intervals]
        actual = Solution().findRightInterval(intervals)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
