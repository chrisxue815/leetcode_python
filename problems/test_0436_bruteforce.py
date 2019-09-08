import sys
import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Brute-force.
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [0] * len(intervals)

        for i, (i_start, i_end) in enumerate(intervals):
            min_val = sys.maxsize
            min_index = -1

            for j, (j_start, j_end) in enumerate(intervals):
                if i == j:
                    continue

                if i_end <= j_start < min_val:
                    min_val = j_start
                    min_index = j

            result[i] = min_index
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
