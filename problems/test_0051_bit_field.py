import unittest


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        board = [['.'] * n for _ in range(n)]
        self.cols = -1
        self.forwards = -1
        self.backwards = -1

        def dfs(row):
            if row == n:
                result.append([''.join(r) for r in board])

            for col in range(n):
                col_mask = 1 << col
                forward_mask = 1 << (row + col)
                backward_mask = 1 << (row - col + n)

                if self.cols & col_mask and self.forwards & forward_mask and self.backwards & backward_mask:
                    self.cols &= ~col_mask
                    self.forwards &= ~forward_mask
                    self.backwards &= ~backward_mask
                    board[row][col] = 'Q'

                    dfs(row + 1)

                    self.cols |= col_mask
                    self.forwards |= forward_mask
                    self.backwards |= backward_mask
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
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
