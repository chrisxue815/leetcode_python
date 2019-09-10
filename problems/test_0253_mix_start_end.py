import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Interval, mixing and sorting start and end.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = [(start, 1) for start, end in intervals] + [(end, -1) for start, end in intervals]
        times.sort()
        result = 0
        curr = 0

        for _, delta in times:
            curr += delta
            result = max(result, curr)

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
