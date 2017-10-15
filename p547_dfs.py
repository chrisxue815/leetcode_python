import unittest


def _set0(m, i):
    m[i][i] = 0
    for j in xrange(len(m)):
        if m[j][j] == 0 or m[i][j] == 0:
            continue
        m[j][j] = 0
        m[i][j] = 0
        _set0(m, j)


# O(n^2) time. O(1) space. DFS.
class Solution(object):
    def findCircleNum(self, m):
        """
        :type m: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(m)):
            if m[i][i] == 0:
                continue
            result += 1
            _set0(m, i)
        return result


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
