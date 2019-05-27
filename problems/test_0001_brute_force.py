import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Brute-force.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                if a + b == target:
                    return [i, i + 1 + j]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().twoSum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
