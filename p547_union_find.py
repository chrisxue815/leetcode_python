import unittest


class UF(object):
    def __init__(self, n):
        self._id = range(n)
        self._sz = [1] * n
        self._count = n

    def find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p

    def union(self, p, q):
        p = self.find(p)
        q = self.find(q)

        if p == q:
            return

        if self._sz[p] < self._sz[q]:
            p, q = q, p

        self._id[q] = p
        self._sz[p] += self._sz[q]
        self._count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self._count


# O(nlog(n)) time. O(n) space. Union-find.
class Solution(object):
    def findCircleNum(self, m):
        """
        :type m: List[List[int]]
        :rtype: int
        """
        uf = UF(len(m))

        for i, row in enumerate(m):
            for j in xrange(i + 1, len(m)):
                if row[j]:
                    uf.union(i, j)

        return uf.count()


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1],
        ], 2)

        self._test([
            [1, 1, 0],
            [1, 1, 1],
            [0, 1, 1],
        ], 1)

        self._test([
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1],
        ], 1)

    def _test(self, m, expected):
        actual = Solution().findCircleNum(m)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
