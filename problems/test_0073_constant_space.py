import unittest


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_top_0 = any(not num for num in matrix[0])
        is_left_0 = any(not matrix[i][0] for i in range(len(matrix)))

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][j]:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for j in range(1, len(matrix[0])):
            if not matrix[0][j]:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        for i in range(1, len(matrix)):
            if not matrix[i][0]:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0

        if is_top_0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if is_left_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0


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
