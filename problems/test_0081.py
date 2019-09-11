import unittest
from typing import List

import utils


# O(log(n)) average, O(n) worst-case time. O(1) space. Binary search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)

            if target == nums[mid]:
                return True

            if nums[mid] < nums[hi]:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif nums[mid] > nums[hi]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                hi -= 1

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().search(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
