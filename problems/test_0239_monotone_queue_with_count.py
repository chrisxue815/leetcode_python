import collections
import unittest
from typing import List

import utils


class MaxQueue:
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


# O(n) time. O(n) space. Monotone queue.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
