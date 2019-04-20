import unittest
import utils

EMPTY = 0
FRESH = 1
ROTTEN = 2


# O(n^2) time. O(n) space. Brute-force.
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        new_grid = [list(row) for row in grid]

        result = 0
        num_fresh = sum(cell == FRESH for row in grid for cell in row)

        def is_adjacent_to_rotten(grid, r, c):
            return (r >= 1 and grid[r - 1][c] == ROTTEN) \
                   or (r + 1 < height and grid[r + 1][c] == ROTTEN) \
                   or (c >= 1 and grid[r][c - 1] == ROTTEN) \
                   or (c + 1 < width and grid[r][c + 1] == ROTTEN)

        while num_fresh:
            new_num_fresh = num_fresh

            for r, row in enumerate(grid):
                for c, cell in enumerate(row):
                    if cell == FRESH and is_adjacent_to_rotten(grid, r, c):
                        new_grid[r][c] = ROTTEN
                        new_num_fresh -= 1
                    else:
                        new_grid[r][c] = cell

            if new_num_fresh == num_fresh:
                return -1

            num_fresh = new_num_fresh
            grid, new_grid = new_grid, grid
            result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().orangesRotting(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
