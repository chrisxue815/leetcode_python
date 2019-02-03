import unittest


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return matrix

        rows = len(matrix)
        cols = len(matrix[0])

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell:
                    if r > 0 and c > 0:
                        matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1]) + 1
                    elif r > 0:
                        matrix[r][c] = matrix[r - 1][c] + 1
                    elif c > 0:
                        matrix[r][c] = matrix[r][c - 1] + 1
                    else:
                        matrix[r][c] = 10000

        for r in xrange(rows - 1, -1, -1):
            for c in xrange(cols - 1, -1, -1):
                if matrix[r][c]:
                    if r + 1 < rows and c + 1 < cols:
                        matrix[r][c] = min(matrix[r + 1][c] + 1, matrix[r][c + 1] + 1, matrix[r][c])
                    elif r + 1 < rows:
                        matrix[r][c] = min(matrix[r + 1][c] + 1, matrix[r][c])
                    elif c + 1 < cols:
                        matrix[r][c] = min(matrix[r][c + 1] + 1, matrix[r][c])

        return matrix


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ], [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ])

        self._test([
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
        ], [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1],
        ])

    def _test(self, matrix, expected):
        actual = Solution().updateMatrix(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
