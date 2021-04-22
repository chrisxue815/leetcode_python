import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array map.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                num = nums[i]
                nums[i], nums[num - 1] = nums[num - 1], nums[i]

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        return len(nums) + 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().firstMissingPositive(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
