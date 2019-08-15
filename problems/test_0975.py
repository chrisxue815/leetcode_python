import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Stack, sorting, DP.
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)

        # next_higher[i] = the index j such that A[j] is the smallest value that satisfies i < j and A[i] <= A[j]
        next_higher = [0] * n

        # next_lower[i]  = the index j such that A[j] is the smallest value that satisfies i < j and A[i] >= A[j]
        next_lower = [0] * n

        stack = []
        for _, j in sorted((a, j) for j, a in enumerate(A)):
            while stack and stack[-1] < j:
                i = stack.pop()
                next_higher[i] = j
            stack.append(j)

        stack = []
        for _, j in sorted((-a, j) for j, a in enumerate(A)):
            while stack and stack[-1] < j:
                i = stack.pop()
                next_lower[i] = j
            stack.append(j)

        # up[i] = 1 if we can start from i, jump up, jump some more times, and reach the end
        up = [0] * n
        up[-1] = 1

        # down[i] = 1 if we can start from i, jump down, jump some more times, and reach the end
        down = [0] * n
        down[-1] = 1

        for i in range(n - 2, -1, -1):
            up[i] = down[next_higher[i]]
            down[i] = up[next_lower[i]]

        return sum(up)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().oddEvenJumps(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
