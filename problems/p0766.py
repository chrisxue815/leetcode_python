import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in xrange(len(matrix) - 1):
            for col in xrange(len(matrix[0]) - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().isToeplitzMatrix(case.matrix)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
