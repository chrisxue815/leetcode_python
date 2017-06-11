import unittest
import collections


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = collections.Counter(s)
        odd = 0
        length = 0
        for count in counts.values():
            odd |= count & 1
            length += count & -2
        return length + odd


class Test(unittest.TestCase):
    def test(self):
        self._test('abccccdd', 7)

    def _test(self, s, expected):
        actual = Solution().longestPalindrome(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
