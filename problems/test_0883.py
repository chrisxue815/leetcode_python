import unittest
import utils


# O(n^2) time. O(n) space. Iteration.
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        max_by_row = [0] * len(grid)
        max_by_col = [0] * len(grid)

        for row, heights in enumerate(grid):
            for col, height in enumerate(heights):
                if height:
                    result += 1
                    max_by_row[row] = max(max_by_row[row], height)
                    max_by_col[col] = max(max_by_col[col], height)

        return result + sum(max_by_row) + sum(max_by_col)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().projectionArea(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
