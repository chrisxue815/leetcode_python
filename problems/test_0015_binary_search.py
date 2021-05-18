import bisect
import collections
import unittest
from typing import List

import utils


# O(n^2) time. O(n) space. Binary search, hash table.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        counts = collections.Counter(nums)
        nums = sorted(counts)

        for i, a in enumerate(nums):
            if a >= 0:
                break
            target = -a
            b_min = target - nums[-1]
            b_max = (target + 1) >> 1
            j_min = bisect.bisect_left(nums, b_min, i + 1)
            j_max = bisect.bisect_left(nums, b_max, j_min)

            for j in range(j_min, j_max):
                b = nums[j]
                c = target - b
                if c in counts:
                    result.append([a, b, c])

        if counts[0] >= 3:
            result.append([0, 0, 0])

        for a, count in counts.items():
            if count >= 2 and a != 0 and -2 * a in counts:
                result.append([a, a, -2 * a])

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        self.assertCountEqual(case.expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
