import bisect
import unittest
from typing import List

import utils


class KeyedSequence:
    def __init__(self, sequence, key_func):
        self.sequence = sequence
        self.key_func = key_func

    def __getitem__(self, i):
        return self.key_func(self.sequence[i])

    def __len__(self):
        return len(self.sequence)


# O(nlog(n)) time. O(n) space. Interval, sorting by start, binary search.
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [0] * len(intervals)
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        keyed_starts = KeyedSequence(starts, lambda start: start[0])

        for i, (start, end) in enumerate(intervals):
            index = bisect.bisect_left(keyed_starts, end)
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
