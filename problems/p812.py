import itertools
import unittest
import utils


def abs_determinant(x, y, z):
    return abs((y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0]))


# O(n^3) time. O(1) space. Math.
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return 0.5 * max(abs_determinant(*triangle) for triangle in itertools.combinations(points, 3))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p812.json').test_cases

        for case in cases:
            actual = Solution().largestTriangleArea(case.points)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()