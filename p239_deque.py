import unittest
import collections


# O(n) time. O(n) space. Deque.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        queue = collections.deque()
        k -= 1

        for i, num in enumerate(nums):
            if queue and queue[0][1] < i - k:
                queue.popleft()

            while queue and queue[-1][0] <= num:
                queue.pop()

            queue.append((num, i))

            if i >= k:
                result.append(queue[0][0])

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])

    def _test(self, nums, k, expected):
        actual = Solution().maxSlidingWindow(nums, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
