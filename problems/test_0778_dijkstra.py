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
        height = len(grid)
        width = len(grid[0])

        result = grid[0][0]
        q = [(result, 0, 0)]

        visited = [[False] * width for _ in range(height)]

        while True:
            depth, row, col = heapq.heappop(q)
            if visited[row][col]:
                continue
            visited[row][col] = True

            if depth > result:
                result = depth

            if row == height - 1 and col == width - 1:
                return result

            if row >= 1 and not visited[row - 1][col]:
                heapq.heappush(q, (grid[row - 1][col], row - 1, col))

            if row + 1 < height and not visited[row + 1][col]:
                heapq.heappush(q, (grid[row + 1][col], row + 1, col))

            if col >= 1 and not visited[row][col - 1]:
                heapq.heappush(q, (grid[row][col - 1], row, col - 1))

            if col + 1 < width and not visited[row][col + 1]:
                heapq.heappush(q, (grid[row][col + 1], row, col + 1))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().swimInWater(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
