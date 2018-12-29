import unittest
import math


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))


class Test(unittest.TestCase):
    def test(self):
        self._test(0, 0)
        self._test(1, 1)
        self._test(2, 1)
        self._test(3, 1)
        self._test(4, 2)
        self._test(5, 2)
        self._test(6, 2)
        self._test(7, 2)
        self._test(8, 2)
        self._test(9, 3)
        self._test(10, 3)

    def _test(self, n, expected):
        actual = Solution().bulbSwitch(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
