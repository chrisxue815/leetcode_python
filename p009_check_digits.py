import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        lo = hi = 1
        while hi * 10 <= x:
            hi *= 10

        while lo < hi:
            if x // lo % 10 != x // hi % 10:
                return False
            lo *= 10
            hi //= 10

        return True


class Test(unittest.TestCase):
    def test(self):
        self._test(1, True)
        self._test(2, True)
        self._test(121, True)
        self._test(1221, True)
        self._test(123, False)
        self._test(1223, False)

    def _test(self, x, expected):
        actual = Solution().isPalindrome(x)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
