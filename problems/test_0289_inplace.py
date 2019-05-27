import unittest


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        height = len(board)
        width = len(board[0])

        for row in range(height):
            for col in range(width):
                live_neighbors = sum(board[row + dr][col + dc] & 1 for dr, dc in neighbors if
                                     0 <= row + dr < height and 0 <= col + dc < width)
                if live_neighbors == 3 or live_neighbors == 2 and board[row][col] & 1:
                    board[row][col] |= 2

        for row in range(height):
            for col in range(width):
                board[row][col] >>= 1


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
