import unittest


def _down_minheap(a, root, hi):
    while True:
        child = root * 2 + 1
        if child >= hi:
            break

        if child + 1 < hi and a[child + 1] < a[child]:
            child += 1

        if a[root] <= a[child]:
            break

        a[root], a[child] = a[child], a[root]
        root = child


def _down_maxheap(a, root, hi):
    while True:
        child = root * 2 + 1
        if child >= hi:
            break

        if child + 1 < hi and a[child + 1] > a[child]:
            child += 1

        if a[root] >= a[child]:
            break

        a[root], a[child] = a[child], a[root]
        root = child


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        k -= 1
        height = len(matrix)
        width = len(matrix[0])

        n = height * width
        if k > n // 2:
            return self.kthLargest(matrix, n - k)

        heap = []
        row0 = matrix[0]
        # Optimization: append the first row on demand
        for j in range(width):
            heap.append((row0[j], 0, j))

        for _ in range(k):
            (val, i, j) = heap[0]
            if i == height - 1:
                heap[0], heap[-1] = heap[-1], heap[0]
                _down_minheap(heap, 0, len(heap) - 1)
                heap.pop()
            else:
                i += 1
                heap[0] = (matrix[i][j], i, j)
                _down_minheap(heap, 0, len(heap))

        return heap[0][0]

    def kthLargest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        k -= 1
        height = len(matrix)
        width = len(matrix[0])

        n = height * width
        if k > n // 2:
            return self.kthSmallest(matrix, n - k)

        heap = []
        row0 = matrix[-1]
        # Optimization: append the first row on demand
        for j in range(width - 1, -1, -1):
            heap.append((row0[j], height - 1, j))

        for _ in range(k):
            (val, i, j) = heap[0]
            if i == 0:
                heap[0], heap[-1] = heap[-1], heap[0]
                _down_maxheap(heap, 0, len(heap) - 1)
                heap.pop()
            else:
                i -= 1
                heap[0] = (matrix[i][j], i, j)
                _down_maxheap(heap, 0, len(heap))

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
