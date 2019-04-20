import unittest
from typing import List

import utils


# O(n * 2^n) time. O(2^n) space. DP.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False

        target = s >> 1
        sums = set()

        for num in nums:
            if num == target:
                return True
            new_sums = []
            for s in sums:
                s += num
                if s == target:
                    return True
                new_sums.append(s)
            sums.add(num)
            sums.update(new_sums)

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
