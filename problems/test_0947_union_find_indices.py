import unittest
from typing import List

import utils


class UnionFind:
    def __init__(self, n):
        self.id = list(range(n))
        self.count = n

    def find(self, p):
        root = p
        while root != self.id[root]:
            root = self.id[root]
        while p != root:
            p, self.id[p] = self.id[p], root
        return root

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)

        if p != q:
            self.id[q] = p
            self.count -= 1

        return p


# O(n) time. O(n) space. Union find, graph.
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(len(stones))
        xs = {}
        ys = {}

        for i, (x, y) in enumerate(stones):
            xid = xs.get(x, None)
            yid = ys.get(y, None)

            if xid is None:
                if yid is None:
                    union_id = i
                else:
                    union_id = uf.union(yid, i)
            else:
                if yid is None:
                    union_id = uf.union(xid, i)
                else:
                    union_id = uf.union(xid, yid)
                    union_id = uf.union(union_id, i)

            xs[x] = union_id
            ys[y] = union_id

        return len(stones) - uf.count


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().removeStones(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
