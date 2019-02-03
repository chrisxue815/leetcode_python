import unittest
import utils


class UnionFind(object):
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
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(len(edges) + 1)

        for edge in edges:
            if not uf.union(*edge):
                return edge


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().findRedundantConnection(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
