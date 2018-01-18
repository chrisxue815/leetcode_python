import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x and not x % 10:
            return False
        y = 0
        while y < x:
            q, r = divmod(x, 10)
            y = y * 10 + r
            x = q
        return x == y or x == y // 10


class Test(unittest.TestCase):
    def test(self):
        self._test(10, False)
        self._test(121, True)
        self._test(1221, True)
        self._test(123, False)
        self._test(1223, False)

    def _test(self, x, expected):
        actual = Solution().isPalindrome(x)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
