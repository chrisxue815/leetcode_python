import unittest
from typing import List

import utils


# O(mn^2) time. O(mn) space. Prefix sum.
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        sums = [[0] * m for _ in range(n + 1)]

        for r, row in enumerate(matrix):
            s = 0
            for c, cell in enumerate(row):
                s += cell
                sums[c + 1][r] = s

        for lo in range(n):
            for hi in range(lo, n):
                lo_col = sums[lo]
                hi_col = sums[hi + 1]
                counts = {0: 1}
                s = 0
                for r in range(m):
                    s += hi_col[r] - lo_col[r]
                    if s - target in counts:
                        result += counts[s - target]
                    if s in counts:
                        counts[s] += 1
                    else:
                        counts[s] = 1

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
