import unittest
from typing import List

import utils


# O(log(n)) time. O(1) space. Binary search.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + ((hi - lo) >> 1)

            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        return nums[hi]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findMin(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
