import itertools
import unittest
import utils


def abs_determinant(x, y, z):
    return abs((y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0]))


# O(n^3) time. O(1) space. Math.
class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return 0.5 * max(abs_determinant(*triangle) for triangle in itertools.combinations(points, 3))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().largestTriangleArea(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
