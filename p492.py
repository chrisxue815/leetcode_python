import unittest
import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while area % w:
            w -= 1

        return [area // w, w]


class Test(unittest.TestCase):
    def test(self):
        self._test(1, [1, 1])
        self._test(2, [2, 1])
        self._test(3, [3, 1])
        self._test(4, [2, 2])
        self._test(5, [5, 1])
        self._test(6, [3, 2])
        self._test(7, [7, 1])
        self._test(8, [4, 2])
        self._test(9, [3, 3])

    def _test(self, n, expected):
        actual = Solution().constructRectangle(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
