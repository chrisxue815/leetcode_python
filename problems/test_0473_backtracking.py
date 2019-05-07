import unittest
from typing import List

import utils


# O(4^n) time. O(n) space. Partition problem, backtracking.
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False

        s = sum(nums)
        side, r = divmod(s, 4)

        if r:
            return False

        sums = [0] * 4

        def dfs(index):
            if index == len(nums):
                return True

            for i in range(4):
                if sums[i] + nums[index] <= side:
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= nums[index]

            return False

        return dfs(0)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().makesquare(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
