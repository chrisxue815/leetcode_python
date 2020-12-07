import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Array.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)

        for r in range(2, rowIndex + 1):
            for c in range(r - 1, 0, -1):
                result[c] += result[c - 1]

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().getRow(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
