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


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        k -= 1
        rows = len(matrix)
        cols = len(matrix[0])

        n = rows * cols
        if k > n // 2:
            return self.kthLargest(matrix, n - k)

        heap = []
        row0 = matrix[0]
        for j in xrange(cols):
            heap.append((row0[j], 0, j))

        for _ in xrange(k):
            (val, i, j) = heap[0]
            if i == rows - 1:
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
        rows = len(matrix)
        cols = len(matrix[0])

        n = rows * cols
        if k > n // 2:
            return self.kthSmallest(matrix, n - k)

        heap = []
        row0 = matrix[-1]
        for j in xrange(cols - 1, -1, -1):
            heap.append((row0[j], rows - 1, j))

        for _ in xrange(k):
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
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
