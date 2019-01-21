import unittest

import utils

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# O(n) time. O(1) space. Logic.
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        direction = 1

        for i in instructions:
            if i == 'G':
                dx, dy = DIRECTIONS[direction]
                x += dx
                y += dy
            elif i == 'L':
                direction = (direction + 1) & 3
            else:
                direction = (direction - 1) & 3

        return x == 0 and y == 0 or direction != 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().isRobotBounded(case.instructions)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
