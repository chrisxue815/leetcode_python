import unittest


def _sift_up(heap, child):
    while True:
        parent = (child - 1) >> 1
        if parent < 0:
            break

        if heap[parent] < heap[child]:
            break

        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent


def _sift_down(heap, root):
    while True:
        child = (root << 1) + 1
        if child >= len(heap):
            break

        right = child + 1
        if right < len(heap) and heap[right] < heap[child]:
            child = right

        if heap[root] <= heap[child]:
            break

        heap[root], heap[child] = heap[child], heap[root]
        root = child


def heappush(heap, item):
    heap.append(item)
    _sift_up(heap, len(heap) - 1)


def heappop(heap):
    last = heap.pop()
    if heap:
        first = heap[0]
        heap[0] = last
        _sift_down(heap, 0)
        return first
    else:
        return last


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

        for i in xrange(len(nums1)):
            heap.append((nums1[i] + nums2[0], i, 0))

        for i in xrange(k):
            if not heap:
                break

            top = heappop(heap)
            i = top[1]
            j = top[2]
            x = nums1[i]
            y = nums2[j]
            result.append([x, y])

            j += 1
            if j < len(nums2):
                x = nums1[i]
                y = nums2[j]
                heappush(heap, (x + y, i, j))

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
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
