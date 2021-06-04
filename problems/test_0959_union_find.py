import unittest
from typing import List

import utils


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        parents = self.parents
        parent = x
        while parent != parents[parent]:
            parent = parents[parent]

        while x != parent:
            x, parents[x] = parents[x], parent

        return parent

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return True
        self.parents[py] = px
        return False


# O(n^2) time. O(n^2) space. Matrix, DFS.
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        result = 1
        n = len(grid)
        m = n + 1
        uf = UnionFind(m * m)
        parents = uf.parents
        for i in (0, m * n):
            for j in range(i, i + m):
                parents[j] = 0
        for i in (0, n):
            for j in range(i, m * m, m):
                parents[j] = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == ' ':
                    continue
                x = m * r + c + (cell == '/')
                y = m * (r + 1) + c + (cell == '\\')
                if uf.union(x, y):
                    result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
