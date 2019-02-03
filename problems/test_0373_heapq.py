import heapq
import unittest


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        result = []
        heap = []

        # Optimization: append the first row on demand
        for i in range(len(nums1)):
            heap.append((nums1[i] + nums2[0], i, 0))

        for i in range(k):
            if not heap:
                break

            top = heap[0]
            i = top[1]
            j = top[2]
            x = nums1[i]
            y = nums2[j]
            result.append([x, y])

            j += 1
            if j < len(nums2):
                x = nums1[i]
                y = nums2[j]
                heap[0] = (x + y, i, j)
                heapq._siftup(heap, 0)
            else:
                heapq.heappop(heap)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 7, 11], [2, 4, 6], 3,
                   [[1, 2], [1, 4], [1, 6]])
        self._test([1, 1, 2], [1, 2, 3], 2,
                   [[1, 1], [1, 1]])
        self._test([1, 2], [3], 3,
                   [[1, 3], [2, 3]])
        self._test([], [], 5, [])

    def _test(self, nums1, nums2, k, expected):
        actual = Solution().kSmallestPairs(nums1, nums2, k)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
