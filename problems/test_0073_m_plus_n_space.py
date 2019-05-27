import unittest


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])

        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if not num:
                    rows[i] = 1
                    cols[j] = 1

        for row, num in enumerate(rows):
            if num:
                for j in range(len(matrix[0])):
                    matrix[row][j] = 0

        for col, num in enumerate(cols):
            if num:
                for i in range(len(matrix)):
                    matrix[i][col] = 0


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [
                [1, 2, 0],
                [1, 2, 3],
                [0, 2, 3],
            ],
            [
                [0, 0, 0],
                [0, 2, 0],
                [0, 0, 0],
            ]
        )

    def _test(self, matrix, expected):
        Solution().setZeroes(matrix)
        self.assertEqual(expected, matrix)


if __name__ == '__main__':
    unittest.main()
