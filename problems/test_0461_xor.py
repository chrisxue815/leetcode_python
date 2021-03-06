import unittest


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x ^= y

        # Hacker's Delight, Figure 5-2
        # See OpenJDK Integer.bitCount():
        # https://github.com/openjdk/jdk/blob/f37d9c8abca50b65ed232831a06d60c1d015013f/src/java.base/share/classes/java/lang/Integer.java#L1685
        x = x - ((x >> 1) & 0x55555555)  # (xx & 01) + ((xx >> 1) & 01) == xx - ((xx >> 1) & 01)
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
        x = (x + (x >> 4)) & 0x0f0f0f0f
        x += x >> 8
        x += x >> 16
        return x & 0x3f


class Test(unittest.TestCase):
    def test(self):
        self._test(0b0000, 0b1010, 2)
        self._test(0b1010, 0b1010, 0)

    def _test(self, x, y, expected):
        self.assertEqual(expected, Solution().hammingDistance(x, y))


if __name__ == '__main__':
    unittest.main()
