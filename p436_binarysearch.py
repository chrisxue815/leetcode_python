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
        starts = []

        for i, interval in enumerate(intervals):
            starts.append((interval.start, i))

        starts.sort(lambda x, y: x[0] - y[0])

        for i in intervals:
            lo = 0
            hi = len(starts) - 1
            end = i.end

            while lo <= hi:
                mid = lo + ((hi - lo) >> 1)
                mid_val = starts[mid][0]

                if mid_val < end:
                    lo = mid + 1
                elif mid_val > end:
                    hi = mid - 1
                else:
                    lo = mid
                    break
            if lo < len(starts):
                result.append(starts[lo][1])
            else:
                result.append(-1)

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
