import unittest


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # Hacker's Delight, Figure 7-1
        # OpenJDK:
        # http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/lang/Integer.java#1145
        n = (n & 0x55555555) << 1 | (n >> 1) & 0x55555555
        n = (n & 0x33333333) << 2 | (n >> 2) & 0x33333333
        n = (n & 0x0f0f0f0f) << 4 | (n >> 4) & 0x0f0f0f0f
        return (n << 24) & 0xffffffff | (n & 0xff00) << 8 | (n >> 8) & 0xff00 | n >> 24


class Test(unittest.TestCase):
    def test(self):
        self._test(2, 0x40000000)
        self._test(43261596, 964176192)

    def _test(self, n, expected):
        actual = Solution().reverseBits(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
