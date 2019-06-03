import unittest
from typing import List

import utils


# O(sum(nums)) time. O(sum(nums)) space. DP, array.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        target = s >> 1
        sums = [False] * target

        for num in nums:
            if num == target:
                return True

            for s in range(target - 1, -1, -1):
                if not sums[s]:
                    continue

                s += num

                if s < target:
                    sums[s] = True
                elif s == target:
                    return True

            if num < target:
                sums[num] = True

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().canPartition(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
