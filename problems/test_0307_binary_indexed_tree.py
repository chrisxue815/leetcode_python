import unittest
from typing import List

import utils


def lowest_bit(val):
    return val & (-val)


# Binary indexed tree.
class NumArray:

    # O(nlog(n) time. O(n) space.
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)

        for i, val in enumerate(nums):
            self._add(i, val)

    # O(log(n)) time. O(1) space.
    def update(self, i: int, val: int) -> None:
        self._add(i, val - self.nums[i])
        self.nums[i] = val

    # O(log(n)) time. O(1) space.
    def sumRange(self, i: int, j: int) -> int:
        return self._sum(j) - self._sum(i - 1)

    # O(log(n)) time. O(1) space.
    def _add(self, i, val):
        x = i + 1
        while x < len(self.tree):
            self.tree[x] += val
            x += lowest_bit(x)

    # O(log(n)) time. O(1) space.
    def _sum(self, i):
        x = i + 1
        s = 0
        while x > 0:
            s += self.tree[x]
            x -= lowest_bit(x)
        return s


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
