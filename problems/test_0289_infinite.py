import unittest
import collections


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width = len(board[0])

        live_cells = set((i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell)

        for i in range(height):
            for j in range(width):
                board[i][j] = 0

        for i, j in self.gameOfLifeInfinite(live_cells):
            if 0 <= i < height and 0 <= j < width:
                board[i][j] = 1

    def gameOfLifeInfinite(self, live_cells):
        neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        num_live_neighbors = collections.Counter((i + di, j + dj) for i, j in live_cells for di, dj in neighbors)

        return (pos for pos, num_neighbors in num_live_neighbors.items() if
                num_neighbors == 3 or num_neighbors == 2 and pos in live_cells)


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ], [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ])

        self._test([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ])

        self._test([
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ], [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0],
        ])

    def _test(self, board, expected):
        Solution().gameOfLife(board)
        self.assertEqual(expected, board)


if __name__ == '__main__':
    unittest.main()
