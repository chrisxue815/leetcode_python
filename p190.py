import unittest


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = n >> 16 | n << 16
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2
        return (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1


class Test(unittest.TestCase):
    def test(self):
        self._test(2, 0x40000000)
        self._test(43261596, 964176192)

    def _test(self, n, expected):
        actual = Solution().reverseBits(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
