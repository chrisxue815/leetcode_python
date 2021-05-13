import unittest
from typing import List

import utils


# O(n) time. O(1) space. Iteration.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0

        for hi, num in enumerate(nums):
            if num:
                nums[lo] = num
                lo += 1

        for lo in range(lo, len(nums)):
            nums[lo] = 0


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, expected, actual, msg, case):
        self.assertEqual(expected, case.args.nums, msg)


if __name__ == '__main__':
    unittest.main()
