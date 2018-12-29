import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0

        def is_magic(ci, cj):
            if not all(1 <= grid[i][j] <= 9 for i in xrange(ci - 1, ci + 2) for j in xrange(cj - 1, cj + 2)):
                return False
            for i in xrange(ci - 1, ci + 2):
                if sum(grid[i][j] for j in xrange(cj - 1, cj + 2)) != 15:
                    return False
            for j in xrange(cj - 1, cj + 2):
                if sum(grid[i][j] for i in xrange(ci - 1, ci + 2)) != 15:
                    return False
            if sum(grid[ci + d][cj + d] for d in xrange(-1, 2)) != 15:
                return False
            if sum(grid[ci - d][cj + d] for d in xrange(-1, 2)) != 15:
                return False

            return True

        for ci in xrange(1, len(grid) - 1):
            for cj in xrange(1, len(grid[0]) - 1):
                if is_magic(ci, cj):
                    result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numMagicSquaresInside(case.grid)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
