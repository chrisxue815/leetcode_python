import heapq
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Interval, sorting intervals by start, saving ends in heap.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        q = []

        for start, end in intervals:
            if q and q[0] <= start:
                heapq.heapreplace(q, end)
            else:
                heapq.heappush(q, end)

        return len(q)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().minMeetingRooms(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
