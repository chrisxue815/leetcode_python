import collections
import unittest
from typing import List

import utils

neighbors = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
]

next_neighbor_indexes = [
    [0, 2, 3],
    [1, 2, 3],
    [0, 1, 2],
    [0, 1, 3],
]


# DFS, BFS.
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()

        def dfs(r, c, mark, neighbor_indexes):
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                return
            grid[r][c] = mark
            if mark == 3:
                q.append((r, c))
            for i in neighbor_indexes:
                dr, dc = neighbors[i]
                dfs(r + dr, c + dc, mark, next_neighbor_indexes[i])

        curr_mark = 2
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    dfs(r, c, curr_mark, [0, 1, 2, 3])
                    curr_mark += 1

        result = 0
        while True:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbors:
                    r2 = r + dr
                    c2 = c + dc
                    if not (0 <= r2 < rows and 0 <= c2 < cols):
                        continue
                    mark = grid[r2][c2]
                    if mark == 2:
                        return result
                    if mark == 0:
                        grid[r2][c2] = curr_mark
                        q.append((r2, c2))
            result += 1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
