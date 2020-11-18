import unittest
from typing import List

import utils


# O(n) time. O(1) space. Linear iteration.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        end = len(nums) - 1
        lo = nums[0]

        for i, hi in enumerate(nums):
            if i == end or hi + 1 != nums[i + 1]:
                if hi == lo:
                    result.append(str(lo))
                else:
                    result.append(str(lo) + '->' + str(hi))
                if i != end:
                    lo = nums[i + 1]

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().summaryRanges(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
