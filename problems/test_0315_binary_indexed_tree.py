import unittest
from typing import List

import utils


def lowest_bit(x):
    return x & -x


class BinaryIndexedTree:
    def __init__(self, n):
        self.nums = [0] * (n + 1)

    def add(self, i, val):
        i += 1
        while i < len(self.nums):
            self.nums[i] += val
            i += lowest_bit(i)

    def sum(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.nums[i]
            i -= lowest_bit(i)
        return result


# O(nlog(n)) time. O(n) space. Binary indexed tree.
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        num_to_order = {num: i for i, num in enumerate(sorted(set(nums)))}
        tree = BinaryIndexedTree(len(nums))

        for i in range(len(nums) - 1, -1, -1):
            order = num_to_order[nums[i]]
            result[i] = tree.sum(order - 1)
            tree.add(order, 1)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countSmaller(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
