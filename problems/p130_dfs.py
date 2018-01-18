import unittest

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


# O(n) time. O(1) space. DFS.
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if board[r][c] != 'O':
                return
            board[r][c] = '1'

            for dr, dc in directions:
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < rows and 0 <= c2 < cols:
                    dfs(r2, c2)

        for r in xrange(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in xrange(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in xrange(rows):
            for c in xrange(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '1':
                    board[r][c] = 'O'


class Test(unittest.TestCase):
    def test(self):
        cases = [
            ([
                 'X X X X',
                 'X O O X',
                 'X X O X',
                 'X O X X',
             ], [
                 'X X X X',
                 'X X X X',
                 'X X X X',
                 'X O X X',
             ]),
        ]

        for case in cases:
            board = [row.split(' ') for row in case[0]]
            expected = [row.split(' ') for row in case[1]]
            Solution().solve(board)
            self.assertEqual(expected, board)


if __name__ == '__main__':
    unittest.main()
