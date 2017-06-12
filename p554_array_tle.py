import unittest
import sys


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        n = len(wall)
        widths = [row[0] for row in wall]
        indices = [0] * n
        min_width = min(widths)
        max_num_edges = 0

        while True:
            next_min_width = sys.maxint
            num_edges = 0
            for i in xrange(n):
                if widths[i] == min_width:
                    num_edges += 1
                    row = wall[i]
                    indices[i] += 1
                    if indices[i] >= len(row):
                        return n - max_num_edges
                    widths[i] += row[indices[i]]
                if widths[i] < next_min_width:
                    next_min_width = widths[i]
            min_width = next_min_width
            if num_edges > max_num_edges:
                max_num_edges = num_edges


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]],
            2)

    def _test(self, wall, expected):
        actual = Solution().leastBricks(wall)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
