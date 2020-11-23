import unittest
from typing import List

import utils


# O(n) time. O(1) space. Matrix, four loops.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        i = 1
        lo = 0
        hi = n - 1

        while lo <= hi:
            for c in range(lo, hi + 1):
                m[lo][c] = i
                i += 1
            for r in range(lo + 1, hi + 1):
                m[r][hi] = i
                i += 1
            for c in range(hi - 1, lo - 1, -1):
                m[hi][c] = i
                i += 1
            for r in range(hi - 1, lo, -1):
                m[r][lo] = i
                i += 1

            lo += 1
            hi -= 1

        return m


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().generateMatrix(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
