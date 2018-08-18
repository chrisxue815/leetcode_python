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
        cases = utils.load_json_from_path('../leetcode_test_cases/p303.json').test_cases

        for case in cases:
            obj = NumArray(case.nums)
            for query in case.queries:
                actual = obj.sumRange(query.i, query.j)
                self.assertEqual(query.expected, actual)


if __name__ == '__main__':
    unittest.main()