import unittest

import utils


# DP, prefix.
class NumArray(object):

    # O(n) time. O(n) space.
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0] * len(nums)
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]
            self.sums[i] = sum_

    # O(1) time. O(1) space.
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - (self.sums[i - 1] if i > 0 else 0)


class Test(unittest.TestCase):
    def test(self):
        cls = NumArray
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
