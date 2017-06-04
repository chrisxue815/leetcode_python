import unittest


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x ^= y

        # Hacker's Delight, Figure 5-2
        # OpenJDK:
        # http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/lang/Integer.java#1082
        x = x - ((x >> 1) & 0x55555555)
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
        self.assertEqual(Solution().hammingDistance(x, y), expected)


if __name__ == '__main__':
    unittest.main()