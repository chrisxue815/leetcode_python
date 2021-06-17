import unittest
from typing import List

import utils


# O(n) time. O(1) space. Greedy.
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result = 0
        miss = 1
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss <<= 1
                result += 1
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
