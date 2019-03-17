import unittest


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Hacker's Delight, Figure 5-2
        # See OpenJDK Integer.bitCount():
        # https://github.com/openjdk/jdk/blob/f37d9c8abca50b65ed232831a06d60c1d015013f/src/java.base/share/classes/java/lang/Integer.java#L1685
        n = n - ((n >> 1) & 0x55555555)  # (xx & 01) + ((xx >> 1) & 01) == xx - ((xx >> 1) & 01)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n + (n >> 4)) & 0x0f0f0f0f
        n += n >> 8
        n += n >> 16
        return n & 0x3f


class Test(unittest.TestCase):
    def test(self):
        self._test(11, 3)

    def _test(self, n, expected):
        actual = Solution().hammingWeight(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
