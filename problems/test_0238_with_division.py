import unittest
from typing import List

import utils


# O(n) time. O(1) space. With division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_index = -1

        for i, num in enumerate(nums):
            if num != 0:
                product *= num
            elif zero_index == -1:
                zero_index = i
            else:
                return [0] * len(nums)

        if zero_index != -1:
            result = [0] * len(nums)
            result[zero_index] = product
            return result

        return [product // num for num in nums]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
