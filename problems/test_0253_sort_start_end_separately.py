import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Interval, sorting start and end separately, merging two sorted lists, two pointers.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(start for start, end in intervals)
        ends = sorted(end for start, end in intervals)

        result = 0
        j = 0

        for start in starts:
            if start < ends[j]:
                result += 1
            else:
                j += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().minMeetingRooms(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
