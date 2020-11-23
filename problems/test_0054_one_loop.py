import unittest

from typing import List

import utils

VISITED = -101


# O(n) time. O(1) space. Matrix, one loop.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        height = len(matrix)
        width = len(matrix[0])
        n = height * width
        result = [0] * n
        r, c, dr, dc = 0, 0, 0, 1

        for i in range(n):
            result[i] = matrix[r][c]
            matrix[r][c] = VISITED
            if matrix[(r + dr) % height][(c + dc) % width] == VISITED:
                dr, dc = dc, -dr
            r += dr
            c += dc

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().spiralOrder(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
