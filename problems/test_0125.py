import unittest


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = 0
        hi = len(s) - 1

        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1

            while lo < hi and not s[hi].isalnum():
                hi -= 1

            if s[lo].lower() != s[hi].lower():
                return False

            lo += 1
            hi -= 1

        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('A man, a plan, a canal: Panama', True)
        self._test('race a car', False)
        self._test('', True)
        self._test('  ', True)

    def _test(self, s, expected):
        actual = Solution().isPalindrome(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
