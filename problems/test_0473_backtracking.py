import unittest
from typing import List

import utils


# O(n!) time. O(n) space. Partition problem, backtracking.
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False

        s = sum(nums)
        side, r = divmod(s, 4)

        if r:
            return False

        def dfs(start, target):
            if start == len(nums):
                return target == 0

            if target == 0:
                target = side

            for i in range(start, len(nums)):
                new_target = target - nums[i]
                if new_target >= 0:
                    nums[start], nums[i] = nums[i], nums[start]

                    if dfs(start + 1, new_target):
                        return True

                    nums[start], nums[i] = nums[i], nums[start]

            return False

        return dfs(0, side)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().makesquare(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
