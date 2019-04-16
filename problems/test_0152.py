import unittest
from typing import List

import utils


# O(n) time. O(1) space. DP.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        left_max = 0
        right_max = 0

        for num in nums:
            left_max = left_max * num if left_max else num
            result = max(result, left_max)

        for num in reversed(nums):
            right_max = right_max * num if right_max else num
            result = max(result, right_max)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().maxProduct(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
