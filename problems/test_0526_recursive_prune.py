import unittest

import utils


def is_beautiful(index, num):
    if index == num:
        return True
    elif index > num:
        return index % num == 0
    else:
        return num % index == 0


# O(n!) time. O(n) space. Backtracking, Recursive permutation.
class Solution:
    def __init__(self):
        self.N = 0
        self.count = 0

    def countArrangement(self, N: int) -> int:
        self.N = N
        self._count(list(range(1, N + 1)), N - 1)
        return self.count

    def _count(self, nums, start):
        if start == -1:
            self.count += 1
        else:
            next_index = start - 1
            index = start + 1
            if is_beautiful(index, nums[start]):
                self._count(nums, next_index)

            for i in range(next_index, -1, -1):
                if is_beautiful(index, nums[i]):
                    nums[i], nums[start] = nums[start], nums[i]
                    self._count(nums, next_index)
                    nums[i], nums[start] = nums[start], nums[i]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countArrangement(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
