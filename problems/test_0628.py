import unittest
from typing import List

import utils


# O(n) time. O(1) space. Math.
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2, max3, min1, min2 = -1000, -1000, -1000, 1000, 1000
        for num in nums:
            if num > max3:
                if num >= max2:
                    if num >= max1:
                        max1, max2, max3 = num, max1, max2
                    else:
                        max2, max3 = num, max2
                else:
                    max3 = num
            if num < min2:
                if num <= min1:
                    min1, min2 = num, min1
                else:
                    min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maximumProduct(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
