import unittest


# O(n) time. O(1) space. Induction.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        n = rows * cols

        result = [0] * n

        top = left = row = col = i = 0
        bottom = rows - 1
        right = cols - 1

        while True:
            if i >= n:
                break
            for col in xrange(col, right + 1):
                result[i] = matrix[row][col]
                i += 1

            if i >= n:
                break
            for row in xrange(row + 1, bottom + 1):
                result[i] = matrix[row][col]
                i += 1

            if i >= n:
                break
            for col in xrange(col - 1, left - 1, -1):
                result[i] = matrix[row][col]
                i += 1

            if i >= n:
                break
            for row in xrange(row - 1, top, -1):
                result[i] = matrix[row][col]
                i += 1

            col += 1
            top += 1
            left += 1
            bottom -= 1
            right -= 1
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], [1, 2, 3, 6, 9, 8, 7, 4, 5])

        self._test([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
        ], [1, 2, 3, 4, 5, 10, 15, 14, 13, 12, 11, 6, 7, 8, 9])

    def _test(self, matrix, expected):
        actual = Solution().spiralOrder(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
