import unittest


class Solution(object):
    def __init__(self):
        self.s = None
        self.n = 0
        self.lo = 0
        self.len = 0

    def _max_palindrome(self, lo, hi):
        while lo >= 0 and hi < self.n and self.s[lo] == self.s[hi]:
            lo -= 1
            hi += 1
        length = hi - lo
        if length > self.len:
            self.len = length
            self.lo = lo

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.n = len(s)

        for i in xrange(self.n):
            self._max_palindrome(i - 1, i + 1)
            self._max_palindrome(i, i + 1)

        return s[self.lo + 1:self.lo + self.len]


class Test(unittest.TestCase):
    def test(self):
        self._test('babad', 'bab')
        self._test('cbbd', 'bb')

    def _test(self, s, expected):
        actual = Solution().longestPalindrome(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
