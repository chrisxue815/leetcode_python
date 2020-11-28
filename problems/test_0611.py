import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Sort, counting pairs in a sorted array.
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        for i in range(2, len(nums)):
            side = nums[i]
            lo = 0
            hi = i - 1

            while lo < hi:
                if nums[lo] + nums[hi] > side:
                    result += hi - lo
                    hi -= 1
                else:
                    lo += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().triangleNumber(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
