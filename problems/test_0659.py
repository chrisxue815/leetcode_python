import heapq
import unittest
from typing import List

import utils


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums:
            return False

        curr_num = nums[0]
        curr_queue = []
        next_queue = []

        for num in nums:
            if num != curr_num:
                if num > curr_num + 1:
                    if next_queue and next_queue[0] < 3:
                        return False
                    next_queue = []
                if curr_queue and curr_queue[0] < 3:
                    return False
                curr_num = num
                curr_queue = next_queue
                next_queue = []

            count = heapq.heappop(curr_queue) if curr_queue else 0
            heapq.heappush(next_queue, count + 1)

        return (not curr_queue or curr_queue[0] >= 3) and (not next_queue or next_queue[0] >= 3)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
