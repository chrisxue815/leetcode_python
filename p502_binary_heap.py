import unittest
import heapq


# O(klog(n)) time. O(n) space. Binary heap.
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capitals):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capitals: List[int]
        :rtype: int
        """
        capital_queue = []
        profit_queue = []

        for i, capital in enumerate(capitals):
            heapq.heappush(capital_queue, (capital, i))

        for _ in xrange(k):
            while capital_queue and capital_queue[0][0] <= w:
                _, i = heapq.heappop(capital_queue)
                heapq.heappush(profit_queue, -profits[i])
            if not profit_queue:
                break
            profit = -heapq.heappop(profit_queue)
            w += profit

        return w


class Test(unittest.TestCase):
    def test(self):
        self._test(2, 0, [1, 2, 3], [0, 1, 1], 4)

    def _test(self, k, w, profits, capitals, expected):
        actual = Solution().findMaximizedCapital(k, w, profits, capitals)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
