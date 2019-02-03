import unittest


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        board = [['.'] * n for _ in xrange(n)]
        cols = [1] * n
        forwards = [1] * (n + n - 1)
        backwards = [1] * (n + n - 1)

        def dfs(row):
            if row == n:
                result.append([''.join(r) for r in board])
            for col in xrange(n):
                if cols[col] and forwards[row + col] and backwards[row - col]:
                    cols[col] = forwards[row + col] = backwards[row - col] = 0
                    board[row][col] = 'Q'
                    dfs(row + 1)
                    cols[col] = forwards[row + col] = backwards[row - col] = 1
                    board[row][col] = '.'

        dfs(0)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(4, [
            ['.Q..',
             '...Q',
             'Q...',
             '..Q.'],
            ['..Q.',
             'Q...',
             '...Q',
             '.Q..']
        ])

    def _test(self, n, expected):
        actual = Solution().solveNQueens(n)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
