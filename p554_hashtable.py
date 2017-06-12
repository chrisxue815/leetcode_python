import unittest
import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        counts = collections.Counter()
        for row in wall:
            width = 0
            for brick in row:
                width += brick
                counts[width] += 1
        most_common = counts.most_common(2)
        return len(wall) - (most_common[1][1] if len(most_common) > 1 else 0)


class Test(unittest.TestCase):
    def test(self):
        self._test([
            [1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [3, 1, 2],
            [1, 3, 1, 1]],
            2)
        self._test([[1], [1], [1]], 3)

    def _test(self, wall, expected):
        actual = Solution().leastBricks(wall)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
