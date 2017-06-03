import unittest


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x ^= y

        # TODO: Hacker's Delight, Figure 5-2
        # OpenJDK:
        # http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/6-b14/java/lang/Integer.java#1082
        count = 0
        while x > 0:
            count += x & 1
            x >>= 1
        return count


class Test(unittest.TestCase):
    def test(self):
        self._test(0b0000, 0b1010, 2)
        self._test(0b1010, 0b1010, 0)

    def _test(self, x, y, expected):
        self.assertEqual(Solution().hammingDistance(x, y), expected)


if __name__ == '__main__':
    unittest.main()
