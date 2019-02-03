import unittest

_a = ord('a')


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        np = len(p)
        ret = []
        cp = [0] * 26
        for ch in p:
            cp[ord(ch) - _a] += 1
        cs = [0] * 26
        for ch in s[:np]:
            cs[ord(ch) - _a] += 1
        if cs == cp:
            ret.append(0)
        lo = 0
        for hi in range(np, len(s)):
            cs[ord(s[lo]) - _a] -= 1
            cs[ord(s[hi]) - _a] += 1
            lo += 1
            if cs == cp:
                ret.append(lo)
        return ret


class Test(unittest.TestCase):
    def test(self):
        self._test('cbaebabacd', 'abc', [0, 6])
        self._test('abab', 'ab', [0, 1, 2])

    def _test(self, s, p, expected):
        actual = Solution().findAnagrams(s, p)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
