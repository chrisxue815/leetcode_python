import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Two pointers.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue

            target = -a
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[j] + nums[k]
                if s == target:
                    result.append([a, nums[j], nums[k]])
                    increase_j = True
                    decrease_k = True
                elif s < target:
                    increase_j = True
                    decrease_k = False
                else:
                    increase_j = False
                    decrease_k = True

                if increase_j:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                if decrease_k:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, expected, actual, msg, case):
        self.assertCountEqual(expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
