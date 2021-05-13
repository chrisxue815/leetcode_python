import unittest

import utils


# O(n^2) time. O(1) space. Palindrome.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_lo = 0
        max_len = 0
        start = 0

        while start < n:
            lo = start - 1
            hi = start + 1

            while hi < n and s[hi] == s[hi - 1]:
                hi += 1

            start = hi

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
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
