import unittest
import heapq


# O(mnlog(m)) time. O(m) space. Binary heap. TLE.
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if m > n:
            m, n = n, m

        heap = []
        for i in xrange(1, m + 1):
            heapq.heappush(heap, (i, i, 1))

        for _ in xrange(k - 1):
            _, i, j = heap[0]
            if j < n:
                heapq.heapreplace(heap, (i * (j + 1), i, j + 1))
            else:
                heapq.heappop(heap)

        return heap[0][0]


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 3, 5, 3)
        self._test(3, 3, 4, 3)
        self._test(2, 3, 6, 6)
        self._test(42, 34, 401, 126)

    def _test(self, m, n, k, expected):
        actual = Solution().findKthNumber(m, n, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
