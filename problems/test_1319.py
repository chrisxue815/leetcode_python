import unittest
from typing import List

import utils


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
        self.components = n

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
        self.components -= 1

        return True

    def connected(self, p, q):
        return self.find(p) == self.find(q)


# O(E*log(V)) time. O(V) space. Graph, union-find.
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)

        for a, b in connections:
            uf.union(a, b)

        return uf.components - 1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
