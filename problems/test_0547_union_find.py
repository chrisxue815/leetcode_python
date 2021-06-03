import unittest
from typing import List

import utils


class UnionFind:
    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n
        self._count = n

    def find(self, p):
        root = p
        while root != self._id[root]:
            root = self._id[root]

        while p != root:
            p, self._id[p] = self._id[p], root

        return root

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)

        if p == q:
            return False

        if self._sz[p] < self._sz[q]:
            p, q = q, p

        self._id[q] = p
        self._sz[p] += self._sz[q]
        self._count -= 1

        return True

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self._count


# O(nlog(n)) time. O(n) space. Union-find.
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))

        for i, row in enumerate(isConnected):
            for j in range(i + 1, len(isConnected)):
                if row[j]:
                    uf.union(i, j)

        return uf.count()


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
