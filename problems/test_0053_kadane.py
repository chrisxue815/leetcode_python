import unittest
from typing import List

import utils


# O(n) time. O(1) space. Kadane's algorithm, greedy.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = max_ending_here = -0x80000000

        for num in nums:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxSubArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
