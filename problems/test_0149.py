import unittest
import itertools
import numpy as np

_inf = float('inf')


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) <= 2:
            return len(points)

        result = 0
        slope_to_count = {}

        for a_index, a in enumerate(points):
            slope_to_count.clear()
            max_count = 0
            for b in itertools.islice(points, a_index + 1):
                dx = b.x - a.x
                dy = b.y - a.y
                if dx:
                    slope = np.longdouble(b.y - a.y) / dx
                elif dy:
                    slope = _inf
                else:
                    max_count += 1
                    continue
                slope_to_count[slope] = slope_to_count.get(slope, 0) + 1

            if slope_to_count:
                max_count += max(slope_to_count.values())
            if max_count > result:
                result = max_count
        return result


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [2, 1],
            [4, 2],
            [6, 3],
            [5, 2],
        ], 3)

        self._test([
            [2, 1],
            [4, 2],
            [6, 3],
            [8, 4],
            [5, 2],
        ], 4)

        self._test([], 0)
        self._test([[0, 0]], 1)
        self._test([[0, 0], [0, 0]], 2)
        self._test([[0, 0], [0, 0], [1, 1]], 3)

        self._test([
            [0, -12], [5, 2], [2, 5], [0, -5], [1, 5], [2, -2], [5, -4],
            [3, 4], [-2, 4], [-1, 4], [0, -5], [0, -8], [-2, -1], [0, -11], [0, -9],
        ], 6)

        self._test([
            [0, 0], [94911151, 94911150], [94911152, 94911151],
        ], 2)

    def _test(self, points, expected):
        actual = Solution().maxPoints([Point(p[0], p[1]) for p in points])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
