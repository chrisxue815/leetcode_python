import unittest
import collections

from typing import List

import utils


# O(n) time. O(n) space. Array, hash table.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
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
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            Solution().gameOfLife(**case.args.__dict__)
            self.assertEqual(case.expected, case.args.board, msg=args)


if __name__ == '__main__':
    unittest.main()
