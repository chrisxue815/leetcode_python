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
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        self._test(matrix, 3, True)
        self._test(matrix, 4, False)

    def _test(self, matrix, target, expected):
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
