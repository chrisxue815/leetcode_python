import unittest
from typing import List

import utils
from tree import TreeNode


# O(mn) time. O(1) space. Space-optimized DP.
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        result = 0
        curr = 0
        start_i = i = len(A) - 1
        start_j = j = 0

        for _ in range(len(A) * len(B)):
            if A[i] == B[j]:
                curr += 1
                result = max(result, curr)

            i += 1
            j += 1

            if i >= len(A) or j >= len(B):
                if start_i > 0:
                    start_i -= 1
                else:
                    start_j += 1

                i = start_i
                j = start_j
                curr = 0

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
