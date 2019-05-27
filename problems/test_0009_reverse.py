import unittest


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y, z = 0, x
        while z:
            q, r = divmod(z, 10)
            y = y * 10 + r  # checking overflow in other languages
            z = q
        return x == y


class Test(unittest.TestCase):
    def test(self):
        self._test(121, True)
        self._test(1221, True)
        self._test(123, False)
        self._test(1223, False)

    def _test(self, x, expected):
        actual = Solution().isPalindrome(x)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
