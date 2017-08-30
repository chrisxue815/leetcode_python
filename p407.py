import unittest
import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        res = 0
        rows = len(heightMap)
        cols = len(heightMap[0])
        visited = [[False] * cols for _ in xrange(rows)]
        q = []

        for row in xrange(rows):
            visited[row][0] = True
            visited[row][cols - 1] = True
            heapq.heappush(q, (heightMap[row][0], row, 0))
            heapq.heappush(q, (heightMap[row][cols - 1], row, cols - 1))
        for col in xrange(cols):
            visited[0][col] = True
            visited[rows - 1][col] = True
            heapq.heappush(q, (heightMap[0][col], 0, col))
            heapq.heappush(q, (heightMap[rows - 1][col], rows - 1, col))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            prev_height, prev_row, prev_col = heapq.heappop(q)
            for delta_row, delta_col in dirs:
                row = prev_row + delta_row
                col = prev_col + delta_col
                if 0 <= row < rows and 0 <= col < cols and not visited[row][col]:
                    visited[row][col] = True
                    height = heightMap[row][col]
                    water_level = max(prev_height, height)
                    res += water_level - height
                    heapq.heappush(q, (water_level, row, col))

        return res


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 4, 3, 1, 3, 2],
            [3, 2, 1, 3, 2, 4],
            [2, 3, 3, 2, 3, 1],
        ], 4)

        self._test([
            [12, 13, 1, 12],
            [13, 4, 13, 12],
            [13, 8, 10, 12],
            [12, 13, 12, 12],
            [13, 13, 13, 13],
        ], 14)

        self._test([
            [5, 5, 5, 1],
            [5, 1, 1, 5],
            [5, 1, 5, 5],
            [5, 2, 5, 8],
        ], 3)

    def _test(self, heights, expected):
        actual = Solution().trapRainWater(heights)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
