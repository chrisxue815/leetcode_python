import unittest
from typing import List

import math

import utils


# O(?) time. O(?) space. Backtracking, integer factorization, combination.
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []

        def dfs(target, start, factors):
            for i in range(start, int(math.sqrt(target)) + 1):
                if target % i == 0:
                    factors.append(i)

                    clone = list(factors)
                    clone.append(target // i)
                    result.append(clone)

                    dfs(target // i, i, factors)

                    factors.pop()

        dfs(n, 2, [])

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().getFactors(**case.args.__dict__)
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
