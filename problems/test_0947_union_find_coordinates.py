import unittest
from typing import List

import utils


class UnionFind(dict):
    def __missing__(self, key):
        self[key] = key
        return key

    def find(self, p):
        root = p
        while root != self[root]:
            root = self[root]
        while p != root:
            p, self[p] = self[p], root
        return root

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)

        self[q] = p


# O(n) time. O(n) space. Union find, graph.
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()

        for x, y in stones:
            uf.union(x, ~y)

        return len(stones) - len({uf.find(i) for i in uf})


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().removeStones(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
