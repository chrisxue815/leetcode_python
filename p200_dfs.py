import unittest


def _set0(grid, i, j):
    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
        grid[i][j] = '0'
        _set0(grid, i - 1, j)
        _set0(grid, i + 1, j)
        _set0(grid, i, j - 1)
        _set0(grid, i, j + 1)


# O(n) time. O(1) space. DFS.
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in xrange(len(grid)):
            row = grid[i]
            for j in xrange(len(row)):
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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
