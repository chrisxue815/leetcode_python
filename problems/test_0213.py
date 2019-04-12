import unittest
from typing import List

import utils


# O(n) time. O(n) space. DP.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums) if nums else 0

        # take1[i]: maximum amount of money you can rob from nums[:i+1], if you rob nums[0]
        take1 = [0] * len(nums)

        # skip1[i]: maximum amount of money you can rob from nums[:i+1], if you don't rob nums[0]
        skip1 = [0] * len(nums)

        take1[0] = nums[0]
        take1[1] = max(take1[0], nums[1])
        skip1[0] = 0
        skip1[1] = nums[1]

        for i in range(2, len(nums) - 1):
            take1[i] = max(take1[i - 1], take1[i - 2] + nums[i])
            skip1[i] = max(skip1[i - 1], skip1[i - 2] + nums[i])

        take1[-1] = take1[-2]
        skip1[-1] = max(skip1[-2], skip1[-3] + nums[-1])

        return max(take1[-1], skip1[-1])


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().rob(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
