import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s = s = sum(nums[:k])
        for i, num in enumerate(nums[k:]):
            s += num - nums[i]
            if s > max_s:
                max_s = s
        return float(max_s) / k


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findMaxAverage(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
