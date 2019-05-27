import unittest
import utils


# O(n) time. O(1) space. Math.
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0

        for row, heights in enumerate(grid):
            for col, height in enumerate(heights):
                if height:
                    result += 2
                    result += max(0, height - grid[row - 1][col]) if row > 0 else height
                    result += max(0, height - grid[row + 1][col]) if row + 1 < len(grid) else height
                    result += max(0, height - grid[row][col - 1]) if col > 0 else height
                    result += max(0, height - grid[row][col + 1]) if col + 1 < len(grid) else height

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().surfaceArea(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
