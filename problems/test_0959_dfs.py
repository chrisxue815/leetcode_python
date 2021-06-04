import unittest
from typing import List

import utils

neighbors = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


# O(n^2) time. O(n^2) space. Matrix, DFS.
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = n * 3
        marks = [[0] * m for _ in range(m)]

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == '/':
                    marks[r * 3][c * 3 + 2] = -1
                    marks[r * 3 + 1][c * 3 + 1] = -1
                    marks[r * 3 + 2][c * 3] = -1
                elif cell == '\\':
                    marks[r * 3][c * 3] = -1
                    marks[r * 3 + 1][c * 3 + 1] = -1
                    marks[r * 3 + 2][c * 3 + 2] = -1

        def dfs(r, c, mark):
            if not (0 <= r < m and 0 <= c < m) or marks[r][c] != 0:
                return
            marks[r][c] = mark

            for dr, dc in neighbors:
                dfs(r + dr, c + dc, mark)

        result = 0
        for r in range(m):
            for c in range(m):
                if marks[r][c] == 0:
                    result += 1
                    dfs(r, c, result)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
