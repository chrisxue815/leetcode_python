import unittest


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m = [[0] * n for _ in range(n)]
        num = 1
        lo = 0
        hi = n

        while lo < hi:
            end = hi - 1
            for i in range(lo, hi):
                m[lo][i] = num
                num += 1
            for i in range(lo + 1, hi):
                m[i][end] = num
                num += 1
            for i in range(end - 1, lo - 1, -1):
                m[end][i] = num
                num += 1
            for i in range(end - 1, lo, -1):
                m[i][lo] = num
                num += 1

            lo += 1
            hi -= 1

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
