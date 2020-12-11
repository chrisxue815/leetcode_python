import unittest
from typing import List

import utils


# O(n) time. O(1) space. Array, iteration.
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        lo = 0

        for hi in range(len(s)):
            if hi == len(s) - 1 or s[hi] != s[hi + 1]:
                if hi - lo >= 2:
                    result.append([lo, hi])
                lo = hi + 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().largeGroupPositions(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
