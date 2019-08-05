import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Brute-force.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            s = nums[i]
            for j in range(i + 1, len(nums)):
                s += nums[j]
                if k == 0:
                    if s == 0:
                        return True
                else:
                    if s % k == 0:
                        return True

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().checkSubarraySum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
