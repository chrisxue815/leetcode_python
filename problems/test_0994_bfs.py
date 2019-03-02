import unittest
import utils

EMPTY = 0
FRESH = 1
ROTTEN = 2


# O(n) time. O(n) space. BFS.
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        q = [(r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == ROTTEN]
        result = 0

        while True:
            new_q = []

            def rot(r, c):
                if grid[r][c] == FRESH:
                    grid[r][c] = ROTTEN
                    new_q.append((r, c))

            for r, c in q:
                if r >= 1:
                    rot(r - 1, c)
                if r + 1 < height:
                    rot(r + 1, c)
                if c >= 1:
                    rot(r, c - 1)
                if c + 1 < width:
                    rot(r, c + 1)

            if new_q:
                q = new_q
                result += 1
            else:
                break

        return result if all(cell != FRESH for row in grid for cell in row) else -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().orangesRotting(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
