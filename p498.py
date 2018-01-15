import unittest


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        size = rows * cols
        ret = [0] * size
        topright = 1
        row = col = 0
        for i in xrange(size):
            ret[i] = matrix[row][col]
            if topright:
                if row and col < cols - 1:
                    row -= 1
                    col += 1
                else:
                    topright = 0
                    if col < cols - 1:
                        col += 1
                    else:
                        row += 1
            else:
                if col and row < rows - 1:
                    row += 1
                    col -= 1
                else:
                    topright = 1
                    if row < rows - 1:
                        row += 1
                    else:
                        col += 1
        return ret


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], [1, 2, 4, 7, 5, 3, 6, 8, 9])

    def _test(self, matrix, expected):
        actual = Solution().findDiagonalOrder(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
