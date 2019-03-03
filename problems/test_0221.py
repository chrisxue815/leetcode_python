import unittest
from typing import List

import utils


# O(n) time. O(n) space. DP.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        height = len(matrix)
        width = len(matrix[0])
        max_ = 0
        h = [[0] * (width + 1) for _ in range(height + 1)]
        v = [[0] * (width + 1) for _ in range(height + 1)]
        dp = [[0] * (width + 1) for _ in range(height + 1)]

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == '1':
                    h[r + 1][c + 1] = h_max = h[r + 1][c] + 1
                    v[r + 1][c + 1] = v_max = v[r][c + 1] + 1
                    dp[r + 1][c + 1] = dp_max = min(dp[r][c] + 1, h_max, v_max)
                    max_ = max(max_, dp_max)
                else:
                    h[r][c] = 0
                    v[r][c] = 0

        return max_ * max_


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().maximalSquare(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
