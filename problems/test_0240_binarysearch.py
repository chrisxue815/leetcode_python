import unittest


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        height = len(matrix)
        width = len(matrix[0])
        top = 0
        right = width - 1

        while True:
            row = matrix[top]
            left = 0
            while left <= right:
                mid = left + ((right - left) >> 1)
                mid_val = row[mid]
                if mid_val < target:
                    left = mid + 1
                elif mid_val > target:
                    right = mid - 1
                else:
                    return True

            if right < 0:
                return False

            bottom = height - 1
            while top <= bottom:
                mid = top + ((bottom - top) >> 1)
                mid_val = matrix[mid][right]
                if mid_val < target:
                    top = mid + 1
                elif mid_val > target:
                    bottom = mid - 1
                else:
                    return True

            if top >= height:
                return False


class Test(unittest.TestCase):
    def test(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self._test(matrix, 5, True)
        self._test(matrix, 20, False)
        self._test([[1, 1]], 2, False)
        self._test([[]], 1, False)
        self._test(
            [[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]],
            19, True)

    def _test(self, matrix, target, expected):
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
