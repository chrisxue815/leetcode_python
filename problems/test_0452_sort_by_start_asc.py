import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by start in ascending order, greedy.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()
        result = 0
        prev_end = points[0][0] - 1

        for start, end in points:
            if prev_end < start:
                result += 1
                prev_end = end
            else:
                prev_end = min(prev_end, end)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findMinArrowShots(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
