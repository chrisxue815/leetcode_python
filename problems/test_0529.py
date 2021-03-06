import unittest


def _eight_neighbors(i, j, height, width):
    if i > 0:
        yield i - 1, j
        if j > 0:
            yield i - 1, j - 1
        if j < width - 1:
            yield i - 1, j + 1
    if i < height - 1:
        yield i + 1, j
        if j > 0:
            yield i + 1, j - 1
        if j < width - 1:
            yield i + 1, j + 1
    if j > 0:
        yield i, j - 1
    if j < width - 1:
        yield i, j + 1


def _reveal(board, digits, i, j):
    if board[i][j] != 'E':
        return

    if digits[i][j]:
        board[i][j] = str(digits[i][j])
        return

    board[i][j] = 'B'

    for ni, nj in _eight_neighbors(i, j, len(board), len(board[0])):
        _reveal(board, digits, ni, nj)


class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        ci, cj = click
        if board[ci][cj] == 'M':
            board[ci][cj] = 'X'
            return board

        height = len(board)
        width = len(board[0])
        digits = [[0] * width for _ in range(height)]

        for i in range(height):
            for j in range(width):
                if board[i][j] == 'M':
                    for ni, nj in _eight_neighbors(i, j, height, width):
                        digits[ni][nj] += 1

        _reveal(board, digits, ci, cj)
        return board


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'M', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
                ['E', 'E', 'E', 'E', 'E'],
            ],
            [3, 0],
            [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B'],
            ]
        )

        self._test(
            [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B'],
            ],
            [1, 2],
            [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'X', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B'],
            ]
        )

    def _test(self, board, click, expected):
        actual = Solution().updateBoard(board, click)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
