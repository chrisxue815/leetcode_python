import unittest
import collections
import heapq


def heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap) - 1)


def heappop_max(heap):
    last = heap.pop()
    if heap:
        ret = heap[0]
        heap[0] = last
        heapq._siftup_max(heap, 0)
    else:
        ret = last
    return ret


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
        if k < len(nums) >> 1:
            for num, count in counts.items():
                if len(heap) < k:
                    heapq.heappush(heap, (count, num))
                elif count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, num))
        else:
            k = len(nums) - k
            for num, count in counts.items():
                if len(heap) < k:
                    heappush_max(heap, (count, num))
                elif count < heap[0][0]:
                    heappop_max(heap)
                    heappush_max(heap, (count, num))
        return [num for _, num in heap]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 1, 2, 2, 3], 2, [1, 2])
        self._test([1], 1, [1])

    def _test(self, nums, k, expected):
        actual = Solution().topKFrequent(nums, k)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
