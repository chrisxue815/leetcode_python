import unittest
from typing import List

import utils


# O(n) time. O(n) space. Partitioning, left and right max arrays.
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []

        result = [0] * (len(nums) - k + 1)
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)
        curr_max = -0x80000000

        for i, num in enumerate(nums):
            if curr_max < num or i % k == 0:
                curr_max = num
            left_max[i] = curr_max

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if curr_max < num or i % k == k - 1:
                curr_max = num
            right_max[i] = curr_max

        for i in range(len(result)):
            result[i] = max(right_max[i], left_max[i + k - 1])

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
