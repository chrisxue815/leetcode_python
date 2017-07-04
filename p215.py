import unittest
import heapq
import itertools


def _kth_largest(nums, k):
    heap = []
    for num in itertools.islice(nums, 0, k):
        heapq.heappush(heap, num)
    for num in itertools.islice(nums, k, len(nums)):
        if num >= heap[0]:
            heapq.heappushpop(heap, num)
    return heap[0]


def _kth_smallest(nums, k):
    heap = []
    for num in itertools.islice(nums, 0, k):
        heap.append(num)
        heapq._siftdown_max(heap, 0, len(heap) - 1)
    for num in itertools.islice(nums, k, len(nums)):
        if num <= heap[0]:
            heapq._heappushpop_max(heap, num)
    return heap[0]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= len(nums) >> 1:
            return _kth_largest(nums, k)
        else:
            return _kth_smallest(nums, len(nums) - k + 1)


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 2, 1, 5, 6, 4], 2, 5)

    def _test(self, nums, k, expected):
        actual = Solution().findKthLargest(nums, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
