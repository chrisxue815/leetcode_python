import bisect
import unittest
from typing import List

import utils


# O(n) time. O(1) space. Binary search
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        nums[i + 1:] = reversed(nums[i + 1:])

        if i < 0:
            return

        j = bisect.bisect_right(nums, nums[i], i + 1)
        if j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            Solution().nextPermutation(**case.args.__dict__)
            self.assertEqual(case.expected, case.args.nums, msg=args)


if __name__ == '__main__':
    unittest.main()
