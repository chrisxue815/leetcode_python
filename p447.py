import unittest
import collections
import math


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        for a in points:
            distances = collections.Counter()
            for b in points:
                diffx = a[0] - b[0]
                diffy = a[1] - b[1]
                distsq = diffx * diffx + diffy * diffy
                distances[distsq] += 1
            for dist in distances.values():
                if dist >= 2:
                    ret += math.factorial(dist) / math.factorial(dist - 2)
        return ret


class Test(unittest.TestCase):
    def test(self):
        self._test([[0, 0], [1, 0], [2, 0]], 2)

    def _test(self, points, expected):
        actual = Solution().numberOfBoomerangs(points)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
