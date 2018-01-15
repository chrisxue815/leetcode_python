import unittest


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        while x != y:
            bit_x = x & 1
            x >>= 1
            bit_y = y & 1
            y >>= 1
            if bit_x != bit_y:
                distance += 1
        return distance


class Test(unittest.TestCase):
    def test(self):
        self._test(0b0000, 0b1010, 2)
        self._test(0b1010, 0b1010, 0)

    def _test(self, x, y, expected):
        self.assertEqual(expected, Solution().hammingDistance(x, y))


if __name__ == '__main__':
    unittest.main()
