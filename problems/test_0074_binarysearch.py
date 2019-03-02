import unittest


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        height = len(matrix)
        width = len(matrix[0])
        n = height * width
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            row, col = divmod(mid, width)
            mid_val = matrix[row][col]
            if mid_val < target:
                lo = mid + 1
            elif mid_val > target:
                hi = mid - 1
            else:
                return True
        return False


class Test(unittest.TestCase):
    def test(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self._test(matrix, 3, True)
        self._test(matrix, 4, False)

    def _test(self, matrix, target, expected):
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
