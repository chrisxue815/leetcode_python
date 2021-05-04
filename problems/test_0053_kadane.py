import unittest
from typing import List

import utils


# O(n) time. O(1) space. Kadane's algorithm, greedy.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -0x80000000
        max_ending_here = 0

        for num in nums:
            max_ending_here = max(max_ending_here + num, num)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
