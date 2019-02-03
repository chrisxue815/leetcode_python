import math
import unittest


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 1:
            return False

        if self._repeated(s, 1):
            return True

        sqrt_l = int(math.sqrt(l))
        for repeated_len in range(2, sqrt_l + 1):
            if l % repeated_len != 0:
                continue
            if self._repeated(s, repeated_len):
                return True
            elif self._repeated(s, l / repeated_len):
                return True
        return False

    def _repeated(self, s, repeated_len):
        for start in range(repeated_len, len(s), repeated_len):
            for i in range(repeated_len):
                if s[i] != s[start + i]:
                    return False
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('abab', True)
        self._test('aba', False)
        self._test('abcabcabcabc', True)
        self._test('abcabdabcabd', True)

    def _test(self, s, expected):
        self.assertEqual(expected, Solution().repeatedSubstringPattern(s))


if __name__ == '__main__':
    unittest.main()
