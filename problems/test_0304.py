import unittest
from typing import List

import utils


# DP, prefix.
class NumMatrix:

    # O(n) time. O(n) space.
    def __init__(self, matrix: List[List[int]]):
        sums = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                s = val
                if r >= 1:
                    s += sums[r - 1][c]
                if c >= 1:
                    s += sums[r][c - 1]
                    if r >= 1:
                        s -= sums[r - 1][c - 1]
                sums[r][c] = s

        self.sums = sums

    # O(1) time. O(1) space.
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.sums[row2][col2]
        if row1 >= 1:
            s -= self.sums[row1 - 1][col2]
        if col1 >= 1:
            s -= self.sums[row2][col1 - 1]
            if row1 >= 1:
                s += self.sums[row1 - 1][col1 - 1]
        return s


class Test(unittest.TestCase):
    def test(self):
        cls = NumMatrix
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
