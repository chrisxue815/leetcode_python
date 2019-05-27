import bisect
import unittest
from typing import List

import utils


# O(n) time. O(1) space. Two pointers.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = bisect.bisect_left(numbers, target - numbers[0], lo=1, hi=len(numbers) - 1)

        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]

            lo += 1
            diff = target - numbers[lo]
            while lo < hi and diff < numbers[hi]:
                hi -= 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().twoSum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
