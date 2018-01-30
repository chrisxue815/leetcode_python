import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        start_row = rows - 1
        start_col = 0

        for _ in xrange(rows + cols - 1):
            num = matrix[start_row][start_col]
            row = start_row + 1
            col = start_col + 1

            while row < rows and col < cols:
                if matrix[row][col] != num:
                    return False
                row += 1
                col += 1

            if start_row > 0:
                start_row -= 1
            else:
                start_col += 1

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p766.json').test_cases

        for case in cases:
            actual = Solution().isToeplitzMatrix(case.matrix)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
