import unittest
from typing import List

import utils


# O(nlog(sum(nums)-max(nums))) time. O(1) space. Binary search.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def num_subarrays_more_than_m(target_sum):
            count = 0
            s = 0
            for num in nums:
                s += num
                if s > target_sum:
                    s = num
                    count += 1
                    if count >= m:
                        return True
            return False

        lo = max(nums)
        hi = sum(nums)

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)

            if num_subarrays_more_than_m(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().splitArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
