import bisect
import unittest
from typing import List

import utils


# Binary search.
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        if rows > cols:
            return self.maxSumSubmatrix(list(zip(*matrix)), k)

        result = -0x80000000

        for ri in range(rows):
            col_sum = [0] * cols
            for rj in range(ri, rows):
                for c, val in enumerate(matrix[rj]):
                    col_sum[c] += val
                curr_sum, prev_sum = 0, [0, 0x7FFFFFFF]
                for val in col_sum:
                    curr_sum += val
                    target = curr_sum - k
                    index = bisect.bisect_left(prev_sum, target)
                    if result < curr_sum - prev_sum[index]:
                        result = curr_sum - prev_sum[index]
                    bisect.insort(prev_sum, curr_sum)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
