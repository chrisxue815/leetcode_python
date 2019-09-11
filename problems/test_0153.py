import unittest
from typing import List

import utils


# O(log(n)) time. O(1) space. Binary search.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            if nums[lo] <= nums[hi]:
                return nums[lo]

            mid = lo + ((hi - lo) >> 1)

            if nums[lo] <= nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findMin(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
