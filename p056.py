import unittest


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]

        for interval in intervals:
            if interval.start <= result[-1].end:
                result[-1].end = max(result[-1].end, interval.end)
            else:
                result.append(interval)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]])

    def _test(self, intervals, expected):
        intervals = [Interval(s, e) for s, e in intervals]

        actual = Solution().merge(intervals)

        actual = [[interval.start, interval.end] for interval in actual]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
