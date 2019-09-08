import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Interval, sorting by end in descending order, greedy.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval[1], reverse=True)
        result = [intervals[0]]

        for start, end in intervals:
            if end < result[-1][0]:
                result.append([start, end])
            else:
                result[-1][0] = min(result[-1][0], start)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().merge(**case.args.__dict__)
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
