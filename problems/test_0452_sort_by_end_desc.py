import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by end in descending order, greedy.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda point: (point[1], point[0]), reverse=True)
        result = 0
        prev_start = points[0][1] + 1

        for s, e in points:
            if e < prev_start:
                result += 1
                prev_start = s
            else:
                prev_start = max(prev_start, s)

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
