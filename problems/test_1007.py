import unittest
from typing import List

import utils


# O(n) time. O(1) space. Counting, set theory.
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        a = [0] * 7
        b = [0] * 7
        c = [0] * 7

        for i in range(n):
            if A[i] == B[i]:
                c[A[i]] += 1
            else:
                a[A[i]] += 1
                b[B[i]] += 1

        for i in range(1, 7):
            if a[i] + b[i] + c[i] >= n:
                return min(n - a[i] - c[i], n - b[i] - c[i])

        return -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().minDominoRotations(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
