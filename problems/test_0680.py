import unittest


def _palindrome(s, lo, hi, tolerate):
    while lo < hi:
        if s[lo] == s[hi]:
            lo += 1
            hi -= 1
        else:
            if not tolerate:
                return False
            return _palindrome(s, lo + 1, hi, False) or _palindrome(s, lo, hi - 1, False)

    return True


# O(n). Two pointers, backtracking.
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return _palindrome(s, 0, len(s) - 1, True)


class Test(unittest.TestCase):
    def test(self):
        self._test('aba', True)
        self._test('abca', True)

    def _test(self, s, expected):
        actual = Solution().validPalindrome(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
