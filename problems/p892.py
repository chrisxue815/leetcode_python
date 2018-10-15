import unittest
import utils


# O(n) time. O(1) space. Math.
class Solution(object):
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
        cases = utils.load_json_from_path('../leetcode_test_cases/p892.json').test_cases

        for case in cases:
            actual = Solution().surfaceArea(case.grid)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
