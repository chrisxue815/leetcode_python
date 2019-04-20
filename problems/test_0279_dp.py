import unittest

import math

import utils

DP = [0, 1]


# O(n * sqrt(n)) time. O(n) space. DP, cheating.
# Better solution: Lagrange's four-square theorem.
# See https://leetcode.com/problems/perfect-squares/discuss/71488
class Solution:
    def numSquares(self, n: int) -> int:
        for num in range(len(DP), n + 1):
            start = int(math.sqrt(num))
            min_ = 0x7fffffff

            for root in range(start, 0, -1):
                count = DP[num - root * root]
                min_ = min(min_, count)
                if min_ <= 1:
                    break

            DP.append(min_ + 1)

        return DP[n]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numSquares(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
