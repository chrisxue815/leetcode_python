import unittest
import utils


# O(mn) time. O(m+n) space. Array.
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_height_by_row_num = [0] * len(grid)
        max_height_by_col_num = [0] * len(grid[0])

        for row_num, row in enumerate(grid):
            for col_num, cell in enumerate(row):
                max_height_by_col_num[col_num] = max(max_height_by_col_num[col_num], cell)
                max_height_by_row_num[row_num] = max(max_height_by_row_num[row_num], cell)

        return sum(min(max_height_by_row_num[row_num], max_height_by_col_num[col_num]) - cell
                   for row_num, row in enumerate(grid) for col_num, cell in enumerate(row))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().maxIncreaseKeepingSkyline(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
