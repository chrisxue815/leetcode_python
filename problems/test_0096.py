import unittest


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1, 1]
        for i in xrange(2, n + 1):
            fi = 0
            for j in xrange(1, i + 1):
                fi += f[j - 1] * f[i - j]
            f.append(fi)

        return f[n]


class Test(unittest.TestCase):
    def test(self):
        self._test(0, 1)
        self._test(1, 1)
        self._test(2, 2)
        self._test(3, 5)
        self._test(4, 14)

    def _test(self, n, expected):
        actual = Solution().numTrees(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
