import unittest
from typing import List

import utils


# O(sum(nums)) time. O(sum(nums)) space. DP, hash set.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        target = s >> 1
        sums = set()
        new_sums = []

        for num in nums:
            if num == target:
                return True

            for s in sums:
                s += num
                if s == target:
                    return True
                new_sums.append(s)

            sums.add(num)
            sums.update(new_sums)
            new_sums.clear()

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
