import unittest
from typing import List

import utils


# O(n) time. O(sum(nums)) space. DP, bit set.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        target = s >> 1
        target_bit = 1 << target
        sums = 1

        for num in nums:
            if num == target:
                return True

            sums |= sums << num

            if sums & target_bit:
                return True

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
