import unittest
from typing import List

import utils


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
        self.count = n

    def find(self, p):
        root = p
        while root != self.parents[root]:
            root = self.parents[root]

        while p != root:
            p, self.parents[p] = self.parents[p], root

        return root

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)

        if p == q:
            return False

        if self.sizes[p] < self.sizes[q]:
            p, q = q, p

        self.parents[q] = p
        self.sizes[p] += self.sizes[q]
        self.count -= 1

        return True

    def connected(self, p, q):
        return self.find(p) == self.find(q)


# O(nlog(n)) time. O(n) space. Union-find.
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))

        for i, row in enumerate(isConnected):
            for j in range(i + 1, len(isConnected)):
                if row[j]:
                    uf.union(i, j)

        return uf.count


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
