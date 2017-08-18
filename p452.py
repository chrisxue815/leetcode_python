import unittest


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort()
        curr = points[0][1]
        count = 1

        for p in points:
            if p[0] > curr:
                curr = p[1]
                count += 1
            elif p[1] < curr:
                curr = p[1]

        return count


class Test(unittest.TestCase):
    def test(self):
        self._test([[10, 16], [2, 8], [1, 6], [7, 12]], 2)
        self._test([[0, 4], [1, 2], [3, 4]], 2)

    def _test(self, points, expected):
        actual = Solution().findMinArrowShots(points)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
