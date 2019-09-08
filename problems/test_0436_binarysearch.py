import unittest
from typing import List

import utils


def bisect_left(starts, target):
    lo = 0
    hi = len(starts) - 1

    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        mid_val = starts[mid][0]
        if mid_val < target:
            lo = mid + 1
        elif mid_val > target:
            hi = mid - 1
        else:
            return mid

    return lo


# O(nlog(n)) time. O(n) space. Interval, sorting by start, binary search.
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [0] * len(intervals)
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))

        for i, (start, end) in enumerate(intervals):
            index = bisect_left(starts, end)
            if index < len(intervals):
                result[i] = starts[index][1]
            else:
                result[i] = -1

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
