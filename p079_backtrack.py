import unittest


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False

        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                if self._dfs(board, word, 0, row, col):
                    return True
                
        return False

    def _dfs(self, board, word, index, row, col):
        next_char = word[index]
        if board[row][col] != next_char:
            return False

        index += 1
        if index == len(word):
            return True

        board[row][col] = 0

        if row >= 1 and self._dfs(board, word, index, row - 1, col):
            return True
        if row < len(board) - 1 and self._dfs(board, word, index, row + 1, col):
            return True
        if col >= 1 and self._dfs(board, word, index, row, col - 1):
            return True
        if col < len(board[0]) - 1 and self._dfs(board, word, index, row, col + 1):
            return True

        board[row][col] = next_char
        return False


class Test(unittest.TestCase):
    def test(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self._test([list(row) for row in board], 'ABCCED', True)
        self._test([list(row) for row in board], 'SEE', True)
        self._test([list(row) for row in board], 'ABCB', False)

    def _test(self, board, word, expected):
        actual = Solution().exist(board, word)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
