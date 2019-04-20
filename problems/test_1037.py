import unittest

import utils


# O(1) time. O(1) space. Geometry.
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        a, b, c = points
        return (b[1] - a[1]) * (c[0] - b[0]) != (b[0] - a[0]) * (c[1] - b[1])


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().isBoomerang(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
