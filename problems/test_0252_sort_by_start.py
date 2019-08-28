import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by start.
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().canAttendMeetings(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
