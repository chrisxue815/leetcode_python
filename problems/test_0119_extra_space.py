import unittest
from typing import List

import utils


# O(n^2) time. O(n) space. Array.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1] * (rowIndex + 1)
        curr = [1] * (rowIndex + 1)

        for r in range(2, rowIndex + 1):
            for c in range(1, r):
                curr[c] = prev[c - 1] + prev[c]
            prev, curr = curr, prev

        return prev


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().getRow(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
