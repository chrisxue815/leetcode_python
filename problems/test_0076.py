import unittest


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or len(s) < len(t):
            return ''

        if len(t) == 1:
            return t if t in s else ''

        counts = [0] * 128

        for ch in t:
            counts[ord(ch)] += 1

        lo = 0
        while lo < len(s) and counts[ord(s[lo])] == 0:
            lo += 1

        num_pending = len(t)
        min_lo = 0
        min_len = len(s) + 1

        for hi in range(lo, len(s)):
            ch = ord(s[hi])

            counts[ch] -= 1
            if counts[ch] >= 0:
                num_pending -= 1

            if num_pending == 0:
                while True:
                    ch = ord(s[lo])
                    lo += 1
                    counts[ch] += 1
                    if counts[ch] == 1:
                        num_pending = 1
                        break

                new_len = hi - lo
                if new_len < min_len:
                    min_len = new_len
                    min_lo = lo

        if min_len > len(s):
            return ''
        return s[min_lo - 1:min_lo + min_len + 1]


class Test(unittest.TestCase):
    def test(self):
        self._test('ADOBECODEBANC', 'ABC', 'BANC')
        self._test('this is a test string', 'tist', 't stri')
        self._test('geeksforgeeks', 'ork', 'ksfor')
        self._test('abc', '', '')
        self._test('abc', 'b', 'b')
        self._test('abc', 'd', '')
        self._test('abc', 'abcd', '')

    def _test(self, s, t, expected):
        actual = Solution().minWindow(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
