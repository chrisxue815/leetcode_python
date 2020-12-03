import unittest
from typing import List

import utils


# O(n^2) time. O(1) space. Array.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        triangle = [[1] * i for i in range(1, numRows + 1)]

        for i in range(3, numRows + 1):
            prev = triangle[i - 2]
            curr = triangle[i - 1]

            for j in range(1, i - 1):
                curr[j] = prev[j - 1] + prev[j]

        return triangle


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().generate(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
