import unittest
import heapq


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return matrix

        rows = len(matrix)
        cols = len(matrix[0])
        q = []
        pending = [[True] * cols for _ in xrange(rows)]

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if not cell:
                    q.append((0, r, c))
                    pending[r][c] = False

        while q:
            distance, r, c = heapq.heappop(q)
            distance += 1

            r2 = r - 1
            if r2 >= 0 and pending[r2][c]:
                pending[r2][c] = False
                matrix[r2][c] = distance
                heapq.heappush(q, (distance, r2, c))

            r2 = r + 1
            if r2 < rows and pending[r2][c]:
                pending[r2][c] = False
                matrix[r2][c] = distance
                heapq.heappush(q, (distance, r2, c))

            c2 = c - 1
            if c2 >= 0 and pending[r][c2]:
                pending[r][c2] = False
                matrix[r][c2] = distance
                heapq.heappush(q, (distance, r, c2))

            c2 = c + 1
            if c2 < cols and pending[r][c2]:
                pending[r][c2] = False
                matrix[r][c2] = distance
                heapq.heappush(q, (distance, r, c2))

        return matrix


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ], [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ])

        self._test([
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1],
        ], [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1],
        ])

    def _test(self, matrix, expected):
        actual = Solution().updateMatrix(matrix)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
