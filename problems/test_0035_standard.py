import unittest
from typing import List

import utils


# O(log(n)) time. O(1) space. Binary search.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                return mid

        return lo


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().searchInsert(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
