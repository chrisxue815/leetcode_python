import unittest


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = 0
        cols = [1] * n
        forwards = [1] * (n + n - 1)
        backwards = [1] * (n + n - 1)

        def dfs(row):
            if row == n:
                self.result += 1
            for col in xrange(n):
                if cols[col] and forwards[row + col] and backwards[row - col]:
                    cols[col] = forwards[row + col] = backwards[row - col] = 0
                    dfs(row + 1)
                    cols[col] = forwards[row + col] = backwards[row - col] = 1

        dfs(0)
        return self.result


class Test(unittest.TestCase):
    def test(self):
        self._test(4, 2)

    def _test(self, n, expected):
        actual = Solution().totalNQueens(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
