import unittest
from typing import List

import utils


# O(D * len(weights)^2) time. O(D * len(weights)) space. Recursion, memorization, TLE.
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        cache = [[-1] * (len(weights) + 1) for _ in range(D + 1)]

        s = 0
        for j, weight in enumerate(weights):
            s += weight
            cache[1][j + 1] = s

        def dfs(i, j):
            if cache[i][j] != -1:
                return cache[i][j]

            mini_max = 0x7fffffff

            for k in range(j):
                mini_max = min(mini_max, max(dfs(i - 1, k), cache[1][j] - cache[1][k]))

            cache[i][j] = mini_max
            return mini_max

        return dfs(D, len(weights))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shipWithinDays(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
