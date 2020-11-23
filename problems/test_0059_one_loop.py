import unittest
from typing import List

import utils


# O(n) time. O(1) space. Matrix, one loop.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        r, c, dr, dc = 0, 0, 0, 1

        for i in range(1, n * n + 1):
            m[r][c] = i
            if m[(r + dr) % n][(c + dc) % n]:
                dr, dc = dc, -dr
            r += dr
            c += dc

        return m


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().generateMatrix(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
