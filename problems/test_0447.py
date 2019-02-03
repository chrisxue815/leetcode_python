import unittest
import collections


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        distances = collections.Counter()
        for a in points:
            for b in points:
                dx = a[0] - b[0]
                dy = a[1] - b[1]
                dist = dx * dx + dy * dy
                distances[dist] += 1
            for count in list(distances.values()):
                if count >= 2:
                    ret += count * (count - 1)
            distances.clear()
        return ret


class Test(unittest.TestCase):
    def test(self):
        self._test([[0, 0], [1, 0], [2, 0]], 2)

    def _test(self, points, expected):
        actual = Solution().numberOfBoomerangs(points)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
