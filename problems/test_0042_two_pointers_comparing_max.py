import unittest
from typing import List

import utils


# O(n) time. O(1) space. Two pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        result = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max < right_max:
                result += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                result += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
