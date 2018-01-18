import unittest
import collections


class MaxQueue(object):
    def __init__(self):
        self.queue = collections.deque()

    def push(self, val):
        count = 1
        while self.queue and self.queue[-1][0] <= val:
            count += self.queue.pop()[1]
        self.queue.append((val, count))

    def pop(self):
        val, count = self.queue[0]
        if count > 1:
            self.queue[0] = (val, count - 1)
        else:
            self.queue.popleft()

    def max(self):
        return self.queue[0][0]


# O(n) time. O(n) space. Monotone priority queue.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        queue = MaxQueue()
        k -= 1
        for i, num in enumerate(nums):
            queue.push(num)
            if i >= k:
                result.append(queue.max())
                queue.pop()
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])

    def _test(self, nums, k, expected):
        actual = Solution().maxSlidingWindow(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
