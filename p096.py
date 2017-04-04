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
        self.assertEqual(Solution().numTrees(0), 1)
        self.assertEqual(Solution().numTrees(1), 1)
        self.assertEqual(Solution().numTrees(2), 2)
        self.assertEqual(Solution().numTrees(3), 5)
        self.assertEqual(Solution().numTrees(4), 14)


if __name__ == '__main__':
    unittest.main()
