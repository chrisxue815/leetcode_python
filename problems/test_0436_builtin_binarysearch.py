import bisect
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Interval, sorting by start, binary search.
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [0] * len(intervals)
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))

        for i, (start, end) in enumerate(intervals):
            index = bisect.bisect_left(starts, (end,))
            result[i] = starts[index][1] if index < len(intervals) else -1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findRightInterval(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
