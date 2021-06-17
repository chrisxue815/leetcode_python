import unittest
from typing import List

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hi = 0
        for lo, num in enumerate(nums):
            if lo > hi:
                return False
            hi = max(hi, lo + num)
        return True


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
