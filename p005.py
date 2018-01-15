import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_lo = 0
        max_len = 0
        i = 0

        while i < n:
            hi = i + 1
            while hi < n and s[hi] == s[hi - 1]:
                hi += 1
            lo = i - 1
            i = hi
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            length = hi - lo
            if length > max_len:
                max_len = length
                max_lo = lo

        return s[max_lo + 1:max_lo + max_len]


class Test(unittest.TestCase):
    def test(self):
        self._test('babad', 'bab')
        self._test('cbbd', 'bb')

    def _test(self, s, expected):
        actual = Solution().longestPalindrome(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
