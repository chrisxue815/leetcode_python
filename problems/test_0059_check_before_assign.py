import unittest


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1

        for num in range(1, n * n + 1):
            m[i][j] = num
            if m[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj

        return m


class Test(unittest.TestCase):
    def test(self):
        self._test(
            3,
            [
                [1, 2, 3],
                [8, 9, 4],
                [7, 6, 5],
            ]
        )

        self._test(
            4,
            [
                [1, 2, 3, 4],
                [12, 13, 14, 5],
                [11, 16, 15, 6],
                [10, 9, 8, 7],
            ]
        )

    def _test(self, n, expected):
        actual = Solution().generateMatrix(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
