import unittest
from typing import List

import utils


# Best case: O(log(n)) time, worst case: O(nlog(n)) time. O(1) space. Binary search.
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            base_val = start - i
            lo = i + 1
            hi = len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) >> 1
                mid_val = nums[mid]
                expected = base_val + mid
                if mid_val > expected:
                    hi = mid - 1
                else:
                    lo = mid + 1
            if hi == i:
                result.append(str(start))
            else:
                result.append(str(start) + '->' + str(base_val + hi))
            i = lo
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
