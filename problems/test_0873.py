import unittest
from typing import List

import utils


# O(n^2) time. O(n^2) space. DP.
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        result = 0
        indexes = {x: i for i, x in enumerate(A)}

        # dp[i][j]: longest path ending in [i, j]
        dp = [[2] * len(A) for _ in range(len(A))]

        for k, z in enumerate(A):
            for j in range(k):
                y = A[j]
                x = z - y
                if x >= y:
                    continue

                i = indexes.get(x, -1)
                if i == -1:
                    continue

                dp[j][k] = dp[i][j] + 1
                result = max(result, dp[j][k])

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().lenLongestFibSubseq(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
