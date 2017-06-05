import unittest


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        if neg:
            x = -x
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x //= 10
        if neg:
            return -y if y <= 0x80000000 else 0
        else:
            return y if y < 0x80000000 else 0


class Test(unittest.TestCase):
    def test(self):
        self._test(123, 321)
        self._test(-123, -321)

    def _test(self, x, expected):
        actual = Solution().reverse(x)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
