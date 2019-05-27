import unittest
import heapq


# O(n^2 * log(n)) time. O(n) space. Binary heap.
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for row in matrix:
            heapq.heappush(heap, (row[0], row, 0))

        for _ in range(k - 1):
            _, row, i = heap[0]
            i += 1
            if i < len(row):
                heapq.heapreplace(heap, (row[i], row, i))
            else:
                heapq.heappop(heap)

        return heap[0][0]


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
        ], 8, 13)

        self._test([
            [1, 2],
            [3, 3],
        ], 2, 2)

        self._test([
            [1, 2],
            [1, 3],
        ], 2, 1)

        self._test([
            [2]
        ], 1, 2)

    def _test(self, matrix, k, expected):
        actual = Solution().kthSmallest(matrix, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
