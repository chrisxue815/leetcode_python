import unittest


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])
        lo = matrix[0][0]
        hi = matrix[-1][-1]

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            count = 0
            j = cols - 1
            for i in xrange(rows):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                if j == -1:
                    break
                count += j + 1
            if count < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
        ], 8, 13)

        self._test([
            [1, 2],
            [3, 3],
        ], 2, 2)

        self._test([
            [1, 2],
            [1, 3],
        ], 2, 1)

        self._test([
            [1, 1],
            [1, 3],
        ], 3, 1)

        self._test([
            [2]
        ], 1, 2)

    def _test(self, matrix, k, expected):
        actual = Solution().kthSmallest(matrix, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
