import heapq
import unittest


class Solution:
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        res = 0
        height = len(heightMap)
        width = len(heightMap[0])
        visited = [[False] * width for _ in range(height)]
        q = []

        for row in range(height):
            visited[row][0] = True
            visited[row][width - 1] = True
            heapq.heappush(q, (heightMap[row][0], row, 0))
            heapq.heappush(q, (heightMap[row][width - 1], row, width - 1))
        for col in range(width):
            visited[0][col] = True
            visited[height - 1][col] = True
            heapq.heappush(q, (heightMap[0][col], 0, col))
            heapq.heappush(q, (heightMap[height - 1][col], height - 1, col))

        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while q:
            prev_height, prev_row, prev_col = heapq.heappop(q)
            for delta_row, delta_col in dirs:
                row = prev_row + delta_row
                col = prev_col + delta_col
                if 0 <= row < height and 0 <= col < width and not visited[row][col]:
                    visited[row][col] = True
                    h = heightMap[row][col]
                    water_level = max(prev_height, h)
                    res += water_level - h
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
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
