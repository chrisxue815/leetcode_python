import unittest


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return any(i == target for row in matrix for i in row)


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

    def _test(self, matrix, target, expected):
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
