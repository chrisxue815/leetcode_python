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
            if height[left] < height[right]:
                if left_max <= height[left]:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if right_max <= height[right]:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
