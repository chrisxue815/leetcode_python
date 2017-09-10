import unittest


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(matrix)
        cols = len(matrix[0])
        state = [[0] * cols for _ in xrange(rows)]

        def dfs(r, c, mask, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or state[r][c] & mask or matrix[r][c] < prev:
                return
            state[r][c] |= mask
            for dr, dc in dirs:
                dfs(r + dr, c + dc, mask, matrix[r][c])

        for c in xrange(cols):
            dfs(0, c, 1, 0)
            dfs(rows - 1, c, 2, 0)

        for r in xrange(rows):
            dfs(r, 0, 1, 0)
            dfs(r, cols - 1, 2, 0)

        for r, row in enumerate(state):
            for c, cell in enumerate(row):
                if cell == 3:
                    result.append([r, c])

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ], [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])

    def _test(self, s, expected):
        actual = Solution().pacificAtlantic(s)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
