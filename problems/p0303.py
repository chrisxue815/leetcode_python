import inspect
import unittest
import utils


# O(1) time. O(n) space. Memorization.
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0] * len(nums)
        sum_ = 0

        for i in xrange(len(nums)):
            sum_ += nums[i]
            self.sums[i] = sum_

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
        functions = {name: func for name, func in inspect.getmembers(cls, predicate=inspect.ismethod)}
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = functions[func](obj, *parameters)
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
