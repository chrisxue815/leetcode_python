import unittest

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


# O(n) time. O(n) space. DFS.
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
        visited = [[False] * cols for _ in xrange(rows)]

        def dfs(r, c):
            if visited[r][c] or board[r][c] == 'X':
                return
            visited[r][c] = True

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
                if not visited[r][c] and board[r][c] == 'O':
                    board[r][c] = 'X'


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
            self.assertEqual(board, expected)


if __name__ == '__main__':
    unittest.main()
