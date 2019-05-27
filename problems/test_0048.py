import unittest


class Solution:
    def rotate(self, m):
        """
        :type m: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(m)
        end = n - 1
        for i in range(n + 1 >> 1):
            for j in range(n >> 1):
                m[i][j], m[j][end - i], m[end - i][end - j], m[end - j][i] = \
                    m[end - j][i], m[i][j], m[j][end - i], m[end - i][end - j]


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
            ],
            [
                [6, 3, 0],
                [7, 4, 1],
                [8, 5, 2],
            ])

        self._test(
            [
                [0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15],
            ],
            [
                [12, 8, 4, 0],
                [13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
            ])

    def _test(self, matrix, expected):
        Solution().rotate(matrix)
        self.assertEqual(expected, matrix)


if __name__ == '__main__':
    unittest.main()
