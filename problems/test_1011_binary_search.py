import unittest
from typing import List

import utils


# O(nlog(sum(weights)-max(weights))) time. O(1) space. Binary search.
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def num_subarrays_more_than_D(target_sum):
            count = 1
            s = 0
            for weight in weights:
                s += weight
                if s > target_sum:
                    count += 1
                    s = weight
                    if count > D:
                        return True
            return False

        lo = max(weights)
        hi = sum(weights)

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if num_subarrays_more_than_D(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shipWithinDays(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
