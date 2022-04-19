import unittest
from typing import List

import utils


# O(n) time. O(1) space. Without division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            result[i + 1] = product

        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            result[i - 1] *= product

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
