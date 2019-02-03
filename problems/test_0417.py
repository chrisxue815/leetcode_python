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
        rows = len(matrix)
        cols = len(matrix[0])
        state = [[0] * cols for _ in range(rows)]

        def dfs(r, c, mask):
            if state[r][c] & mask:
                return

            state[r][c] |= mask
            height = matrix[r][c]

            r2 = r - 1
            if r2 >= 0 and matrix[r2][c] >= height:
                dfs(r2, c, mask)

            r2 = r + 1
            if r2 < rows and matrix[r2][c] >= height:
                dfs(r2, c, mask)

            c2 = c - 1
            if c2 >= 0 and matrix[r][c2] >= height:
                dfs(r, c2, mask)

            c2 = c + 1
            if c2 < cols and matrix[r][c2] >= height:
                dfs(r, c2, mask)

        for c in range(cols):
            dfs(0, c, 1)
            dfs(rows - 1, c, 2)

        for r in range(rows):
            dfs(r, 0, 1)
            dfs(r, cols - 1, 2)

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
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
