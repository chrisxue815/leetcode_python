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

            l = max(ll, ls + rl)
            m = max(lm, rm, lr + rl)
            r = max(rr, rs + lr)
            s = ls + rs

            return l, m, r, s

        _, result, _, _ = dfs(0, len(nums))

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxSubArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
