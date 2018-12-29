import unittest


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        n = 1440
        minutes = [0] * n
        for timepoint in timePoints:
            minute = int(timepoint[:2]) * 60 + int(timepoint[3:])
            minutes[minute] += 1
            if minutes[minute] > 1:
                return 0

        for i in xrange(n):
            if minutes[i] == 1:
                break

        first = i
        prev = i
        min_gap = n

        for i in xrange(i + 1, n):
            if minutes[i] == 1:
                gap = i - prev
                if gap < min_gap:
                    min_gap = gap
                prev = i

        gap = first + n - prev
        if gap < min_gap:
            min_gap = gap

        return min_gap


class Test(unittest.TestCase):
    def test(self):
        self._test(["23:59", "00:00"], 1)
        self._test(["23:59", "23:59"], 0)

    def _test(self, timePoints, expected):
        actual = Solution().findMinDifference(timePoints)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
