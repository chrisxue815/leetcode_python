import unittest
import utils


# O(mn) time. O(n) space. DFS.
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        rows = len(grid)
        cols = len(grid[0])

        def mark_live(row, col):
            if grid[row][col] != 1:
                return 0

            grid[row][col] = 2
            count = 1

            if row >= 1:
                count += mark_live(row - 1, col)
            if row + 1 < rows:
                count += mark_live(row + 1, col)
            if col >= 1:
                count += mark_live(row, col - 1)
            if col + 1 < cols:
                count += mark_live(row, col + 1)

            return count

        def is_live(row, col):
            return row == 0 or grid[row - 1][col] == 2 \
                   or row + 1 < rows and grid[row + 1][col] == 2 \
                   or col >= 1 and grid[row][col - 1] == 2 \
                   or col + 1 < cols and grid[row][col + 1] == 2

        for hit_row, hit_col in hits:
            grid[hit_row][hit_col] -= 1

        for top_col in xrange(cols):
            mark_live(0, top_col)

        result = [0] * len(hits)

        for i in xrange(len(hits) - 1, -1, -1):
            hit_row, hit_col = hits[i]

            if grid[hit_row][hit_col] != 0:
                continue

            grid[hit_row][hit_col] = 1

            if is_live(hit_row, hit_col):
                count = mark_live(hit_row, hit_col)
                result[i] = count - 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().hitBricks(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
