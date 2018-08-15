import heapq
import unittest
import utils


# O(nlog(n)) time. O(n) space. Dijkstra.
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        result = grid[0][0]
        q = [(result, 0, 0)]

        visited = [[False] * cols for _ in xrange(rows)]

        while True:
            depth, row, col = heapq.heappop(q)
            if visited[row][col]:
                continue
            visited[row][col] = True

            if depth > result:
                result = depth

            if row == rows - 1 and col == cols - 1:
                return result

            if row >= 1 and not visited[row - 1][col]:
                heapq.heappush(q, (grid[row - 1][col], row - 1, col))

            if row + 1 < rows and not visited[row + 1][col]:
                heapq.heappush(q, (grid[row + 1][col], row + 1, col))

            if col >= 1 and not visited[row][col - 1]:
                heapq.heappush(q, (grid[row][col - 1], row, col - 1))

            if col + 1 < cols and not visited[row][col + 1]:
                heapq.heappush(q, (grid[row][col + 1], row, col + 1))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p778.json').test_cases

        for case in cases:
            actual = Solution().swimInWater(case.grid)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
