import unittest
from typing import List

import utils
from tree import TreeNode


# O(mn) time. O(mn) space. DP.
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        result = 0

        # dp[i][j]: maximum length of an subarray that ends with A[i-1] and B[j-1]
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findLength(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
