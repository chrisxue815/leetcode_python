import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        cols = len(board[0])

        def move_up(r, c):
            for r in xrange(r - 1, -1, -1):
                yield r, c

        def move_down(r, c):
            for r in xrange(r + 1, rows):
                yield r, c

        def move_left(r, c):
            for c in xrange(c - 1, -1, -1):
                yield r, c

        def move_right(r, c):
            for c in xrange(c + 1, cols):
                yield r, c

        rock_row, rock_col = next((r, c) for r, row in enumerate(board) for c, cell in enumerate(row) if cell == 'R')
        result = 0

        for move in [move_up, move_down, move_left, move_right]:
            for r, c in move(rock_row, rock_col):
                cell = board[r][c]

                if cell == 'B':
                    break
                elif cell == 'p':
                    result += 1
                    break

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numRookCaptures(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
