import unittest
from typing import List

import utils

neighbors = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]

next_neighbor_indexes = [
    [0, 1, 2, 3, 5],
    [0, 1, 2],
    [0, 1, 2, 4, 7],
    [0, 3, 5],
    [2, 4, 7],
    [0, 3, 5, 6, 7],
    [5, 6, 7],
    [2, 4, 5, 6, 7],
]

digits = [str(i) for i in range(9)]
digits[0] = 'B'


# O(n) time. O(n) space. Recursive DFS.
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cx, cy = click
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
            return board

        rows = len(board)
        cols = len(board[0])

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def reveal(r, c, neighbor_indexes):
            if not valid(r, c) or board[r][c] != 'E':
                return

            mines = 0
            for i in neighbor_indexes:
                dr, dc = neighbors[i]
                if valid(r + dr, c + dc) and board[r + dr][c + dc] == 'M':
                    mines += 1

            board[r][c] = digits[mines]

            if not mines:
                for i, (dr, dc) in enumerate(neighbors):
                    reveal(r + dr, c + dc, next_neighbor_indexes[i])

        reveal(cx, cy, range(8))
        return board


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
