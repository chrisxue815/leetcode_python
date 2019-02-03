import unittest
import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums
        counts = collections.Counter(nums)
        heap = []
        for num, count in list(counts.items()):
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))
        return [num for _, num in heap]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 1, 2, 2, 3], 2, [1, 2])
        self._test([1], 1, [1])

    def _test(self, nums, k, expected):
        actual = Solution().topKFrequent(nums, k)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
