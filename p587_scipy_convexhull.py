import unittest
import itertools
import scipy.spatial


# O(nlog(n)) time. SciPy ConvexHull (Qhull, Quickhull).
class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        try:
            tuples = [(p.x, p.y) for p in points]
            hull = scipy.spatial.ConvexHull(tuples, qhull_options='Qc')
            return [points[i] for i in itertools.chain(hull.vertices, hull.coplanar[:, 0])]
        except scipy.spatial.qhull.QhullError:
            return points


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Test(unittest.TestCase):
    def test(self):
        self._test([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
                   [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]])

        self._test([[1, 2], [2, 2], [4, 2]],
                   [[1, 2], [2, 2], [4, 2]])

    def _test(self, points, expected):
        points = [Point(x, y) for x, y in points]
        actual = Solution().outerTrees(points)
        actual = [[p.x, p.y] for p in actual]
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
