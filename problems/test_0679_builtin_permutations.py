import unittest
import itertools


def _dfs(nums):
    if len(nums) == 1:
        # For Python 3.5+, use math.isclose
        return abs(nums[0] - 24) < 1e-3

    for p in itertools.permutations(nums):
        a, b, c = p[0], p[1], p[2:]
        if a <= b:
            if _dfs((a + b,) + c):
                return True
            if _dfs((a * b,) + c):
                return True
        if _dfs((a - b,) + c):
            return True
        if b and _dfs((a / b,) + c):
            return True
    return False


# n! * (n-1)! * ... * 1! * 4^n time. O(1) space. Backtracking.
class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [float(num) for num in nums]
        return _dfs(nums)


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 1, 8, 7], True)
        self._test([1, 2, 1, 2], False)
        self._test([3, 3, 8, 8], True)

    def _test(self, nums, expected):
        actual = Solution().judgePoint24(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
