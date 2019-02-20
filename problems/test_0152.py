import unittest
from typing import List

import utils


def calc_max_product(a, b, c, d, e):
    if b == 0:
        return a
    if d == 0:
        if c >= 0:
            return max(a, c)
        else:
            return (a if a else 1) * b * c
    if c >= 0:
        return (a if a else 1) * b * (c if c else 1) * d * (e if e else 1)
    else:
        return max((a if a else 1) * b * c, e, a, c * d * (e if e else 1))


# O(n) time. O(1) space. Logic.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        result = 0
        a = b = c = d = e = 0

        for num in nums:
            if num > 0:
                if e:
                    e *= num
                else:
                    e = num
            elif num < 0:
                if d < 0:
                    c = (c if c else 1) * d * (e if e else 1)
                    d = num
                elif b < 0:
                    c = e
                    d = num
                else:
                    a = e
                    b = num
                e = 0
            else:
                if b == 0:
                    a = e
                    e = 0
                elif d == 0:
                    c = e
                    e = 0
                result = max(result, calc_max_product(a, b, c, d, e))
                a = b = c = d = e = 0

        if b == 0:
            a = e
            e = 0
        elif d == 0:
            c = e
            e = 0
        result = max(result, calc_max_product(a, b, c, d, e))

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().maxProduct(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
