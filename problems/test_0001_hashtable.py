import unittest
from typing import List

import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().twoSum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
