import unittest
from typing import List

import utils


# O(n) time. O(log(n)) space. Divide and conquer.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(lo, length):
            if length == 1:
                return nums[lo], nums[lo], nums[lo], nums[lo]

            half = length >> 1
            ll, lm, lr, ls = dfs(lo, half)
            rl, rm, rr, rs = dfs(lo + half, length - half)

            # max sum that starts with lo
            l = max(ll, ls + rl)
            # max sum of any subarray
            m = max(lm, rm, lr + rl)
            # max sum that ends with lo + length
            r = max(rr, rs + lr)
            # sum
            s = ls + rs

            return l, m, r, s

        _, result, _, _ = dfs(0, len(nums))

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
