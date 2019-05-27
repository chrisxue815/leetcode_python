import unittest


# O(n). DFS.
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        height = len(grid)
        width = len(grid[0])

        def dfs(row, col):
            if 0 <= row < height and 0 <= col < width and grid[row][col]:
                grid[row][col] = 0
                return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
            else:
                return 0

        for row in range(height):
            for col in range(width):
                area = dfs(row, col)
                if area > result:
                    result = area

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ], 6)

        self._test([
            [0, 0, 0, 0, 0, 0, 0, 0],
        ], 0)

    def _test(self, grid, expected):
        actual = Solution().maxAreaOfIsland(grid)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
