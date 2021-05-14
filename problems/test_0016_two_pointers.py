import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Two pointers.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = 0x7FFFFFFF
        closest = 0
        nums.sort()

        for i in range(len(nums) - 2):
            a = nums[i]
            s = a + nums[i + 1] + nums[i + 2]
            if s >= target:
                if abs(s - target) < min_diff:
                    return s
                return closest

            s = a + nums[-2] + nums[-1]
            if i > 0 and nums[i - 1] == a or s <= target:
                if s == target:
                    return s
                if abs(s - target) < min_diff:
                    min_diff = abs(s - target)
                    closest = s
                continue

            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                s = a + nums[lo] + nums[hi]
                if abs(s - target) < min_diff:
                    min_diff = abs(s - target)
                    closest = s
                if s < target:
                    if a + (nums[hi] << 1) < target:
                        break
                    lo += 1
                elif s > target:
                    if a + (nums[lo] << 1) > target:
                        break
                    hi -= 1
                else:
                    return s

        return closest


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
