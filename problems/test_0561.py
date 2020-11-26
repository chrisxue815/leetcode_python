import unittest
import itertools
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Sort.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        return sum(itertools.islice(nums, 0, len(nums), 2))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().arrayPairSum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
