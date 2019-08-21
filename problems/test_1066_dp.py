import sys
import unittest
from typing import List

import utils


# O(n * 2^m * m) time. O(n * 2^m) space. DP, bit set.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)
        m = len(bikes)

        # dp[i][j]: the minimum sum of Manhattan distances between workers[:i] and their assigned bike.
        # If the k-th bit of j is set, it means the k-th bike is taken.
        dp = [[sys.maxsize] * (1 << m) for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, 1 << m):
                for k in range(m):
                    if j & (1 << k) == 0:
                        continue
                    prev = j ^ (1 << k)
                    s = abs(workers[i - 1][0] - bikes[k][0]) + abs(workers[i - 1][1] - bikes[k][1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][prev] + s)

        return min(dp[n])


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().assignBikes(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
