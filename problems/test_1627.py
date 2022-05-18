import unittest
from typing import List

import utils


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n

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
            return

        if self.sizes[p] < self.sizes[q]:
            p, q = q, p

        self.parents[q] = p
        self.sizes[p] += self.sizes[q]

    def connected(self, p, q):
        return self.find(p) == self.find(q)


# O(E*log(n)) time. O(n) space. Number theory, union-find.
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n + 1)

        for i in range(threshold + 1, n + 1):
            for j in range(2, n // i + 1):
                uf.union(i, i * j)

        return [uf.connected(x, y) for x, y in queries]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        for i, query in enumerate(case.args.queries):
            self.assertEqual(case.expected[i], actual[i], query)


if __name__ == '__main__':
    unittest.main()
