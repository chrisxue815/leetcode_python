import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Monotone queue.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
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
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
