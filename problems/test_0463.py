import unittest


# O(n) time. O(1) space.
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        islands = neighbors = 0
        for i, row in enumerate(grid):
            for j in range(width):
                if row[j]:
                    islands += 1
                    if i + 1 < height and grid[i + 1][j]:
                        neighbors += 1
                    if j + 1 < width and row[j + 1]:
                        neighbors += 1
        return islands * 4 - neighbors * 2


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]],
            16)

    def _test(self, grid, expected):
        actual = Solution().islandPerimeter(grid)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
