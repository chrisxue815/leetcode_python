import unittest


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = 0
        self.cols = -1
        self.forwards = -1
        self.backwards = -1
        board = [['.'] * n for _ in xrange(n)]

        def dfs(row):
            if row == n:
                self.result += 1

            for col in xrange(n):
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
        return self.result


class Test(unittest.TestCase):
    def test(self):
        self._test(4, 2)

    def _test(self, n, expected):
        actual = Solution().totalNQueens(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
