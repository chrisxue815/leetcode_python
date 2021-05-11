import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Brute-force.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if a + nums[j] == target:
                    return [i, j]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)
