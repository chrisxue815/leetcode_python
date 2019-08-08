import unittest
from typing import List

import utils


# O(mn^2) time. O(mn) space. Recursion, memorization, TLE.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        cache = [[0] * (n + 1) for _ in range(m + 1)]

        for j, num in enumerate(nums):
            cache[1][j + 1] = cache[1][j] + num

        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]

            mini_max = 0x7fffffff

            for k in range(j):
                mini_max = min(mini_max, max(dfs(i - 1, k), cache[1][j] - cache[1][k]))

            cache[i][j] = mini_max
            return mini_max

        return dfs(m, n)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().splitArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
