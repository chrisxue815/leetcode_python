import unittest
from typing import List

import utils


# O(n) time. O(n) space.
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)

        max_so_far = 0
        for i, h in enumerate(height):
            max_left[i] = max_so_far = max(max_so_far, h)

        result = 0
        max_so_far = 0
        for i in range(len(height) - 1, -1, -1):
            max_so_far = max(max_so_far, height[i])
            limit = min(max_left[i], max_so_far)
            result += limit - height[i]

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
