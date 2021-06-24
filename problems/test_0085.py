import unittest
from typing import List

import utils


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * (n + 1)
        result = 0

        for row in matrix:
            for c, cell in enumerate(row):
                heights[c] = heights[c] + 1 if cell == '1' else 0

            stack = [-1]
            for c, h in enumerate(heights):
                while h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = c - 1 - stack[-1]
                    result = max(result, height * width)
                stack.append(c)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
