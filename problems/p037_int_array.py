import unittest


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = [[1] * 10 for _ in xrange(9)]
        cols = [[1] * 10 for _ in xrange(9)]
        blocks = [[1] * 10 for _ in xrange(9)]

        for rownum, row in enumerate(board):
            for colnum, num in enumerate(row):
                if num != '.':
                    num = int(num)
                    rows[rownum][num] = cols[colnum][num] = blocks[rownum // 3 * 3 + colnum // 3][num] = 0

        def dfs(rownum, colnum):
            while True:
                if colnum < 8:
                    colnum += 1
                elif rownum < 8:
                    colnum = 0
                    rownum += 1
                else:
                    return True
                if board[rownum][colnum] == '.':
                    break

            row = rows[rownum]
            col = cols[colnum]
            block = blocks[rownum // 3 * 3 + colnum // 3]
            for num in xrange(1, 10):
                if row[num] and col[num] and block[num]:
                    row[num] = col[num] = block[num] = 0
                    if dfs(rownum, colnum):
                        board[rownum][colnum] = str(num)
                        return True
                    row[num] = col[num] = block[num] = 1
            return False

        dfs(0, -1)


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ], [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ])

    def _test(self, board, expected):
        board = [[str(num) if num != 0 else '.' for num in row] for row in board]

        Solution().solveSudoku(board)

        board = [[int(num) for num in row] for row in board]
        self.assertEqual(expected, board)


if __name__ == '__main__':
    unittest.main()
