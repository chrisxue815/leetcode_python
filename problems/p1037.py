import unittest

import numpy as np

import utils


# O(1) time. O(1) space. Geometry.
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        a, b, c = points

        if a == b or b == c or a == c:
            return False

        grad_ab = np.float32(b[1] - a[1]) / (b[0] - a[0])
        grad_bc = np.float32(c[1] - b[1]) / (c[0] - b[0])

        return not np.isclose(grad_ab, grad_bc)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().isBoomerang(case.points)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
