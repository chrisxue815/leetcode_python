import unittest
from typing import List

import utils


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])
        result = [0] * (m * n)
        r = 0
        c = 0
        top_right = True

        for i in range(m * n):
            result[i] = matrix[r][c]

            if top_right:
                if c == n - 1:
                    r += 1
                    top_right = False
                elif r == 0:
                    c += 1
                    top_right = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    top_right = True
                elif c == 0:
                    r += 1
                    top_right = True
                else:
                    r += 1
                    c -= 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findDiagonalOrder(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
