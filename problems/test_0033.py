import unittest
from typing import List

import utils


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]

            if target == mid_val:
                return mid

            lo_val = nums[lo]
            hi_val = nums[hi]

            if lo_val <= mid_val:
                if lo_val <= target <= mid_val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if mid_val <= target <= hi_val:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().search(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
