import collections
import unittest
from typing import List

import utils


# O(n^2) time. O(n) space. DP, sort, ordered dict.
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subsets = collections.OrderedDict()
        max_count = 0
        max_factor = 0

        for num in nums:
            half = num >> 1
            prev_count = 0
            prev_factor = 0

            for factor, (count, _) in subsets.items():
                if factor > half:
                    break
                if prev_count < count and num % factor == 0:
                    prev_count = count
                    prev_factor = factor

            prev_count += 1
            subsets[num] = (prev_count, prev_factor)

            if max_count < prev_count:
                max_count = prev_count
                max_factor = num

        result = [0] * max_count
        curr = max_factor
        for i in range(max_count - 1, -1, -1):
            result[i] = curr
            _, curr = subsets[curr]

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().largestDivisibleSubset(**case.args._asdict())
            self.assertIn(actual, case.expected)


if __name__ == '__main__':
    unittest.main()
