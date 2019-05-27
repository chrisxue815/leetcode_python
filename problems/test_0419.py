import unittest


class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == 'X' and (not r or board[r - 1][c] != 'X') and (not c or board[r][c - 1] != 'X'):
                    result += 1
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([
            'X..X',
            '...X',
            '...X',
        ], 2)

    def _test(self, board, expected):
        actual = Solution().countBattleships(board)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
