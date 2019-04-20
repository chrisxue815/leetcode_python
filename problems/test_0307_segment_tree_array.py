import unittest
from typing import List

import utils


# https://graphics.stanford.edu/~seander/bithacks.html#RoundUpPowerOf2
def round_up_to_power_of_2(v):
    v -= 1
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >> 16
    return v + 1


# O(n) space. Segment tree array.
class NumArray:
    # O(n) time. O(1) space.
    def __init__(self, nums: List[int]):
        num_leaves = round_up_to_power_of_2(len(nums))
        leaf_start = num_leaves - 1
        tree = [0] * (leaf_start + num_leaves)

        for i, val in enumerate(nums):
            tree[leaf_start + i] = val

        for x in range(leaf_start - 1, -1, -1):
            tree[x] = tree[x * 2 + 1] + tree[x * 2 + 2]

        self.nums = nums
        self.num_leaves = num_leaves
        self.tree = tree

    # O(log(n)) time. O(1) space.
    def update(self, i: int, val: int) -> None:
        tree = self.tree
        delta = val - self.nums[i]
        self.nums[i] = val

        x = 0
        lo = 0
        hi = self.num_leaves - 1

        while x < len(tree):
            tree[x] += delta
            mid = lo + (hi - lo) // 2
            if i <= mid:
                x = x * 2 + 1
                hi = mid
            else:
                x = x * 2 + 2
                lo = mid

    # O(log(n)) time. O(log(n)) space.
    def sumRange(self, i: int, j: int) -> int:
        tree = self.tree

        def dfs(x, lo, hi):
            if i <= lo and hi <= j:
                return tree[x]

            s = 0
            mid = lo + (hi - lo) // 2

            if i <= mid:
                s += dfs(x * 2 + 1, lo, mid)
            if mid < j:
                s += dfs(x * 2 + 2, mid + 1, hi)

            return s

        return dfs(0, 0, self.num_leaves - 1)


class Test(unittest.TestCase):
    def test(self):
        cls = NumArray
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
