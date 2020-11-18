import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array, bit manipulation.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
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
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            Solution().gameOfLife(**case.args.__dict__)
            self.assertEqual(case.expected, case.args.board, msg=args)


if __name__ == '__main__':
    unittest.main()
