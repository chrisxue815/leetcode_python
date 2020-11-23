import unittest

from typing import List

import utils


# O(n) time. O(1) space. Matrix.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        height = len(matrix)
        width = len(matrix[0])
        n = height * width

        result = [0] * n

        top = left = i = 0
        bottom = height - 1
        right = width - 1

        while True:
            for col in range(left, right + 1):
                result[i] = matrix[top][col]
                i += 1
            if i >= n:
                break
            top += 1

            for row in range(top, bottom + 1):
                result[i] = matrix[row][right]
                i += 1
            if i >= n:
                break
            right -= 1

            for col in range(right, left - 1, -1):
                result[i] = matrix[bottom][col]
                i += 1
            if i >= n:
                break
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                result[i] = matrix[row][left]
                i += 1
            if i >= n:
                break
            left += 1

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
