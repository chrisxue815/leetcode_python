import unittest
import fractions


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return not z or z <= x + y and not z % fractions.gcd(x, y)


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 5, 4, True)
        self._test(2, 6, 5, False)
        self._test(0, 0, 0, True)
        self._test(1, 1, 0, True)
        self._test(1, 0, 0, True)
        self._test(0, 1, 0, True)
        self._test(0, 0, 1, False)
        self._test(1, 0, 1, True)
        self._test(0, 1, 1, True)
        self._test(2, 0, 1, False)
        self._test(1, 2, 3, True)

    def _test(self, x, y, z, expected):
        actual = Solution().canMeasureWater(x, y, z)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
