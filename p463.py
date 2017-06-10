import unittest


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        peri = 0
        for i in xrange(height):
            for j in xrange(width):
                if grid[i][j]:
                    if not i or not grid[i - 1][j]:
                        peri += 1
                    if i == height - 1 or not grid[i + 1][j]:
                        peri += 1
                    if not j or not grid[i][j - 1]:
                        peri += 1
                    if j == width - 1 or not grid[i][j + 1]:
                        peri += 1
        return peri


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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
