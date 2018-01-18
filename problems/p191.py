import unittest


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Hacker's Delight, Figure 5-2
        # OpenJDK:
        # http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/lang/Integer.java#1082
        n = n - ((n >> 1) & 0x55555555)
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
