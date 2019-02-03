import unittest


def _set0(grid, i, j):
    grid[i][j] = '0'
    if i >= 1 and grid[i - 1][j] == '1':
        _set0(grid, i - 1, j)
    if i + 1 < len(grid) and grid[i + 1][j] == '1':
        _set0(grid, i + 1, j)
    if j >= 1 and grid[i][j - 1] == '1':
        _set0(grid, i, j - 1)
    if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
        _set0(grid, i, j + 1)


# O(n) time. O(1) space. DFS.
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(row)):
                if row[j] == '1':
                    result += 1
                    _set0(grid, i, j)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([
            '11110',
            '11010',
            '11000',
            '00000',
        ], 1)

        self._test([
            '11000',
            '11000',
            '00100',
            '00011',
        ], 3)

    def _test(self, grid, expected):
        grid = [list(row) for row in grid]
        actual = Solution().numIslands(grid)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
