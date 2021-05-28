import unittest
from typing import List

import utils


# O(n) time. O(n) space. DFS.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        height = len(matrix)
        width = len(matrix[0])

        max_lengths = [[0] * width for _ in range(height)]

        def dfs(row, col):
            max_length = max_lengths[row][col]
            if max_length:
                return max_length

            curr = matrix[row][col]
            max_length = 0

            if row > 0 and matrix[row - 1][col] > curr:
                max_length = max(max_length, dfs(row - 1, col))

            if row + 1 < height and matrix[row + 1][col] > curr:
                max_length = max(max_length, dfs(row + 1, col))

            if col > 0 and matrix[row][col - 1] > curr:
                max_length = max(max_length, dfs(row, col - 1))

            if col + 1 < width and matrix[row][col + 1] > curr:
                max_length = max(max_length, dfs(row, col + 1))

            max_length += 1
            max_lengths[row][col] = max_length
            return max_length

        return max(dfs(row, col) for row in range(height) for col in range(width))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
