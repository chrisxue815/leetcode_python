import unittest
import utils


# O(n) time. O(n) space. DFS.
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        max_lengths = [[0] * cols for _ in range(rows)]

        def dfs(row, col):
            max_length = max_lengths[row][col]
            if max_length:
                return max_length

            curr = matrix[row][col]
            max_length = 0

            if row > 0 and matrix[row - 1][col] > curr:
                max_length = max(max_length, dfs(row - 1, col))

            if row + 1 < rows and matrix[row + 1][col] > curr:
                max_length = max(max_length, dfs(row + 1, col))

            if col > 0 and matrix[row][col - 1] > curr:
                max_length = max(max_length, dfs(row, col - 1))

            if col + 1 < cols and matrix[row][col + 1] > curr:
                max_length = max(max_length, dfs(row, col + 1))

            max_length += 1
            max_lengths[row][col] = max_length
            return max_length

        return max(dfs(row, col) for row in range(rows) for col in range(cols))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().longestIncreasingPath(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
