import unittest
from typing import List

import utils


# O(n) space. DP, prefix.
class NumArray:

    # O(n) time. O(1) space.
    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]
            self.sums[i] = sum_

    # O(1) time. O(1) space.
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left > 0 else 0)


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, NumArray)


if __name__ == '__main__':
    unittest.main()
