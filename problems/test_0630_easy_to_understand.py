import heapq
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Interval, sorting by end, greedy.
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])

        time = 0
        q = []

        for t, d in courses:
            if time + t <= d:
                heapq.heappush(q, -t)
                time += t
            elif q and t < -q[0]:
                longer_course = -heapq.heappop(q)
                heapq.heappush(q, -t)
                time += t - longer_course

        return len(q)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().scheduleCourse(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
